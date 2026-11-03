# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

**1. The request arrives (`POST /submit` in `app.py`).** A client sends the text to the service as JSON, for example `{"text": "...", "creator_id": "..."}`. Flask receives it and turns the JSON body into a Python dictionary with `request.get_json()`. **It adds** a readable form of the submission that the rest of the code can work with. Before this step it's just bytes over the network. After it, there's a dict holding the `text` and the `creator_id` of whoever sent it. Nothing has been judged yet.

**2. The submission is unpacked and given an ID (`submit()` in `app.py`).** The handler takes `text` and `creator_id` out of the dictionary and checks them against the contract below. Text that is missing, not a string, blank, under 50 characters or over 20,000 is turned away here with a 4xx error and a plain-language message, and so is a missing `creator_id`. Nothing bad reaches a later step, and nothing turned away is logged as a decision. It then creates a `content_id` with `uuid.uuid4()`. **It adds** a unique ID for this one submission. Every later step, the log entry, and any appeal the writer files will use this ID to refer to it.

**3. The model signal (`detector.model_signal` in `detector.py`).** The text is run through GPT-2 on the local machine to measure its perplexity, meaning how predictable the model finds each next word. That perplexity is squashed onto a 0–1 scale, where low perplexity means a high score. **It adds** `model_score`, a number from 0 to 1 where higher means "reads more like AI." This step judges the words themselves, not the shape of the text.

**4. The style signal (`stylometry.style_signal` in `stylometry.py`).** The same text is measured as shape only, without reading its meaning. It takes four measures: how much sentence lengths vary, how often vocabulary repeats, how much human-leaning punctuation there is, and how often em dashes and colons appear. Each is placed on a 0–1 "AI-ness" scale between a typical-human and a typical-AI value, and they're averaged with weights set by calibration (sentence spread counts most). Alongside it, `phrases.phrase_signal` counts stock AI phrases and adds a `phrase_score` (stretch goal). **It adds** `style_score`, a second 0–1 score where higher means "more like AI." It comes from a completely different kind of evidence than step 3.

**5. The two signals are combined (`scoring.combine_signals` in `scoring.py`).** The two scores are averaged with equal weight, and the phrase score can nudge that average toward AI by up to 20% of the distance left. If either the model or the style signal leans human (below 0.5), the result is capped at 0.64, just under the AI threshold, so a disagreement can produce "unsure" but never an AI label. The full rule is under *Signals and Scoring* below. **It adds** `combined_score`, one number from 0 (confidently human) to 1 (confidently AI). Every later decision is based on this number.

**6. The score becomes words (`scoring.score_to_label` in `scoring.py`).** The combined score is compared against two thresholds in `config.py`, `HUMAN_THRESHOLD` and `AI_THRESHOLD`. The comparison puts it in one of three bands: high-confidence human (0.35 or below), unsure, or high-confidence AI (0.65 or above). **It adds** a `guess` (`human` / `unsure` / `ai`) for the machine, a `label`, which is the plain-language sentence a reader actually sees in place of a number (the exact wording is under *Label Variants*), and a `confidence`, which says how far the score sits from the 0.5 midpoint.

**7. The decision is logged and returned (`audit.log_decision` in `audit.py`, then the JSON response).** The service writes one line to the append-only audit log. That line holds the timestamp, `content_id`, `creator_id`, both signal scores, the combined score, the guess, the label, and the status `decided`. It then sends the same information back to the caller as JSON. **It adds** a permanent record of the decision that can be checked later and that `/appeal` can find by `content_id`. The response also delivers the label to the reader, which is the end of the path.

**After the label: the appeal (`POST /appeal`).** If the writer thinks the label is wrong, they send the `content_id` and their reasoning. The service checks that the ID exists (404 if not), writes an appeal entry with status `under_review` right after the original decision, and confirms. The original decision is never changed or deleted, and nothing is re-scored automatically; a person reviews it.

### Tracing the false positive

**The writer.** A student writing in their second language submits a paragraph they wrote themselves. They stick to words they're sure of and keep sentences short and similar so they don't make grammar mistakes. Every word is theirs.

**Step 3, model signal.** Common words in ordinary sentences are exactly what GPT-2 predicts well, so perplexity comes out low, around 25. Using the formula in `detector.py` (midpoint 45, steepness 1.6), that gives a `model_score` of about **0.72**.

**Step 4, style signal.** The sentences are all about the same length, the vocabulary repeats, and the punctuation is just periods and commas. On every measure that's the "even" shape this signal reads as AI. Say `style_score` ≈ **0.70**.

**Step 5, combine.** With the placeholder 50/50 average, `combined_score` ≈ **0.71**. The two signals don't cancel each other out, because they share the same blind spot: plain, careful writing looks predictable *and* looks even. A second signal only protects the writer if it fails on different text than the first one.

**Step 6, label.** 0.71 is above `AI_THRESHOLD` (0.65), so `guess` is `ai` and the writer sees the **high-confidence AI** label. To them it reads as an accusation, with a sure-sounding tone about something false. Nothing in the label tells them why it was flagged or that they can push back.

**Step 7, log.** The decision is recorded with status `decided` and their `content_id`.

**What they can do.** Their only route is `POST /appeal` with their `content_id` and a written explanation. That records the appeal and moves the item to `under_review`. The original decision stays in the log, nothing is re-scored automatically, and a person has to look at it. This only works if the writer knows the appeal exists, has kept their `content_id`, and feels able to argue in a language they're less sure of. Those are hardest for exactly the writers most likely to be flagged.

**What this decides.** With the current numbers, an honest writer can land well inside "high-confidence AI" with no warning. That pushes my thresholds and rule in three directions:
- `AI_THRESHOLD` has to sit high enough that plainly written human text lands in **unsure**, not AI. I'll test this in Milestone 4 with a plain human paragraph as a calibration input.
- The combining rule shouldn't let two signals with the same blind spot add up to certainty.
- The AI label, and the unsure label most of all, should tell the reader how to appeal and should never state authorship as fact.

### The endpoints

The contract every other piece has to keep. All bodies are JSON. Every error looks the same, `{"error": "<code>", "message": "<sentence for a person>"}`, which matches the 429 response already in `app.py`. Bad input always gets a 4xx, never a 500.

#### `POST /submit`

**In**

| Field | Type | Required | Rule |
|---|---|---|---|
| `text` | string | yes | The writing to check. At least 50 characters after trimming whitespace. At most 20,000 characters. |
| `creator_id` | string | yes | Who submitted it. Not empty. Used for the log, appeals, and (in unit 8) rate limiting. |

Only the first ~400 tokens (about 300 words) reach the model signal (`DETECTOR_MAX_TOKENS`). The style signal reads the whole text.

**Out: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | New UUID for this submission. The writer needs it to appeal. |
| `creator_id` | string | Echoed back from the request. |
| `guess` | string | `"human"`, `"unsure"`, or `"ai"`. |
| `label` | string | The exact sentence the reader sees. |
| `confidence` | float 0–1 | How far the combined score sits from the 0.5 midpoint: `abs(combined_score − 0.5) × 2`. Near 0 means the signals give no clear answer. Near 1 means a strong lean one way. |
| `combined_score` | float 0–1 | Output of `combine_signals`. Higher means more AI-like. |
| `model_score` | float 0–1 | Signal one. Higher means more AI-like. Required: unit 8's tools read it. |
| `style_score` | float 0–1 | Signal two. Higher means more AI-like. Required: unit 8's tools read it. |
| `phrase_score` | float 0–1 | Signal three (stretch goal). Stock AI phrases per 100 words, scaled. Higher means more AI-like. |
| `status` | string | Always `"decided"` on a new submission. |

**Errors**

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body isn't a JSON object. |
| 400 | `missing_text` | `text` is absent, not a string, or empty after trimming. |
| 400 | `text_too_short` | Under 50 characters. Too little to score honestly, and the detector refuses under 3 tokens. |
| 413 | `text_too_long` | Over 20,000 characters. |
| 400 | `missing_creator_id` | `creator_id` is absent, not a string, or empty. |
| 429 | `rate_limited` | Unit 8, once limiting is on. Already handled in `app.py`. |
| 503 | `detector_unavailable` | The model couldn't load (`DetectorUnavailable`). Nothing is logged as a decision. |

#### `POST /appeal`

**In**

| Field | Type | Required | Rule |
|---|---|---|---|
| `content_id` | string | yes | Must match a submission already in the log (`audit.entries_for`). |
| `reasoning` | string | yes | The writer's explanation, in their own words. Not empty. At most 5,000 characters. |

The request doesn't take a `creator_id`. The service copies it from the original decision in the log, so the appeal is always tied to the person who submitted.

**Out: `200 OK`**

| Field | Type | Meaning |
|---|---|---|
| `content_id` | string | Echoed back. |
| `status` | string | `"under_review"`. |
| `message` | string | Plain confirmation to the writer that a person will look at it. Nothing is re-scored automatically. |

An appeal on an item already under review is accepted and logged again. The log is append-only, so every appeal is kept.

**Errors**

| Status | `error` | When |
|---|---|---|
| 400 | `invalid_json` | The body isn't a JSON object. |
| 400 | `missing_content_id` | `content_id` is absent or empty. |
| 400 | `missing_reasoning` | `reasoning` is absent, empty, or over 5,000 characters. |
| 404 | `unknown_content_id` | No submission with that ID in the log. Says so plainly instead of failing silently. |

#### `GET /content/<content_id>` (stretch goal)

**In:** the `content_id` in the URL. No body.

**Out: `200 OK`:** `content_id`, `status` (from the most recent log entry: `decided`, or `under_review` once appealed), `submitted_at`, the original `guess`, `label`, `model_score`, `style_score`, `phrase_score` and `combined_score`, and `appeals`, a list of `{timestamp, reasoning}` that's empty if there are none. Everything comes from the audit log, so it can't disagree with it. `phrase_score` is `null` for items scored before the phrase signal existed.

**Errors:** 404 `unknown_content_id` if no submission has that ID.


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** How predictable the text is to a language model. `detector.py` runs GPT-2 locally and computes the text's **perplexity**, meaning how surprised the model is by each next word on average. It then maps that onto 0–1, where low perplexity (very predictable) means a high, AI-like score. A perplexity of about 45 scores 0.5.

**Why that might differ between human and AI writing:** A language model writes by repeatedly picking a likely next word, so text a model produced tends to be text a model finds easy to predict. Human writing wanders more, with odd word choices, sudden turns, and specific details where a model would use typical ones. All of that raises perplexity. AI text also leans on the same safe choices again and again: stock transitions like "It is important to note" or "In conclusion," and a familiar set of words like *delve*, *testament*, and *intricate*. Phrases a model uses often are, by definition, phrases a model predicts easily.

**What it can't see:** Who actually wrote the text. Predictability is not authorship. What this signal really rewards is **common words in short, ordinary sentences**, and many real people write that way: someone writing in a second language and sticking to words they're sure of, a younger writer, or anyone writing plainly on purpose. Their honest writing can score as AI-like as machine text. It also fails the other way. Dense, ornate prose full of rare words scores as *human* because rare words are hard to predict, so an AI asked to write in an unusual style, or AI text with a few uncommon words swapped in, can slip through. The same goes for stock phrases. Students are taught to write "In conclusion" and to follow a five-paragraph essay outline, and second-language writers often rely on set phrases because they know those phrases are correct. Formulaic does not mean machine-written. The writers this signal is most likely to wrongly accuse are the ones with the least room to argue back.

### Signal two — the style signal

**What it measures:** The *shape* of the text, without reading what it says. `stylometry.py` combines four measures into one 0–1 score where higher means more AI-like:
- **Sentence length spread:** do sentence lengths vary, or are they all about the same? Higher means more human.
- **Type-token ratio:** what fraction of the words are distinct, or how much the vocabulary repeats. Measured over a sliding 50-word window so long and short texts compare fairly. Higher means more human.
- **Punctuation density:** commas, semicolons, parentheses, `?`, `!` and typed dashes (`-`, `--`) per word. Higher means more human.
- **Dash and colon rate:** em dashes (—), en dashes (–) and colons per word. These are kept separate because they point the other way: recent chat models overuse them. Higher means more AI.

**Why that might differ between human and AI writing:** Generated prose tends toward even, medium-length sentences, a narrower vocabulary, and tidy, standard punctuation, because "most likely next word" produces average-shaped text. Human writing is lumpier: a three-word sentence next to a forty-word one, a favorite word repeated, a dash or parenthesis or exclamation mark where it feels right. Published linguistic comparisons back this up: human texts show more variation in sentence length and sentence structure, while AI output leans formal and evenly structured, with more dense, noun-heavy phrasing.

**What it can't see:** Meaning. This signal cannot read. It has no idea what the text says or who wrote it, so anything that changes the shape without changing the substance moves the score. Examples are adding typos, splitting or merging sentences, adding dashes and semicolons, or pasting in a quotation. That makes it cheap to fool on purpose: lightly editing AI text this way can push it toward "human." It also misjudges people whose natural style is even and tidy, such as a careful writer following a style guide or someone writing a short, structured answer. Their text has the regular shape this signal reads as AI-like. Short texts are another weak point, because with only a few sentences these measures are mostly noise. The dash and colon rate also can't tell a chat model from a person whose phone or word processor turns `--` into `—` automatically. The popular rule that "quirks and flaws mean human" is exactly this weakness. It rewards anyone who adds a few typos, and it penalizes the careful human writer who fixed theirs. Finally, a lot of what really separates human writing is out of reach for both signals because it depends on meaning: emotional depth, sarcasm, a specific remembered detail, an unresolved thought, or whether the reasoning holds up.

### Signal three — the phrase signal (stretch goal)

**What it measures:** Stock phrases and favourite words that chat models fall back on, counted per 100 words. `phrases.py` matches a list of 28 patterns, such as "it is important to", "in today's fast-paced", "one of the most important", "ultimately,", "additionally,", "a testament to", "delve" and "plays a crucial role". Zero hits scores 0. Two or more per 100 words scores 1. Higher means more AI-like.

**Why that might differ between human and AI writing:** A model tuned to sound helpful and polished reaches for the same safe transitions and impressive-sounding words again and again. On my calibration inputs, both versions of the AI essay had five or six stock phrases in about 250 words. My abstract, my journal entry and my short messages had none.

**What it can't see:** Anything not on its list. It's the easiest of the three to fool: delete or swap the phrases and it reads 0. The list also ages as new models pick up new habits. And people use these phrases too. Students are taught "In conclusion" and "Additionally", and second-language writers lean on set phrases because they know they're correct. That's the same writer my false-positive trace follows.

**How the three are weighted against each other:** Model and style are the two real votes, averaged with equal weight. The phrase signal is not a third vote in that average. It's a **one-way nudge** applied after it: it moves the score toward 1 by at most 20% of the distance left (`WEIGHT_PHRASE_SIGNAL = 0.2`).
- **Why it can only push toward AI:** a phrase score of 0 is weak evidence of anything, because plenty of AI text has no stock phrases. Counting 0 as "human" would quietly lower every score and undo my calibration.
- **Why it's capped at 20%:** it's the easiest signal to fool and the one most likely to catch a formulaic student.
- **Why it has no say in the split rule:** the AI label still needs both model and style to lean AI, so stock phrases alone can never get a writer accused. The most they can do is move a text that both main signals already lean AI on a little further.

Effect on my inputs: every human and unsure result is unchanged, because none of my writing has stock phrases. The AI essay moved from 0.8021 to 0.8417, and the edited AI essay from 0.7846 to 0.8274.

### Calibration

Four inputs, each run through `detector.model_signal` and the `stylometry.py` measures. Each style measure shows its raw value, then its 0–1 AI-ness against the anchors in `stylometry.ANCHORS`. Higher model and style scores mean more AI-like.

| Input | Words | Words/sentence | Model | Spread | Vocabulary | Punctuation | Dash/colon | Style |
|---|---|---|---|---|---|---|---|---|
| Clearly AI (written by Claude, unedited) | 251 | 15.7 | **0.887** | 0.238 → 1.00 | 0.850 → 0.00 | 0.072 → 0.78 | 0.000 → 0.00 | **0.718** |
| Lightly edited AI (the same text, edited by me) | 252 | 15.8 | **0.863** | 0.227 → 1.00 | 0.851 → 0.00 | 0.079 → 0.71 | 0.000 → 0.00 | **0.706** |
| Clearly human (my own paper abstract, formal) | 171 | 34.2 | **0.413** | 0.941 → 0.00 | 0.850 → 0.00 | 0.117 → 0.33 | 0.006 → 0.19 | **0.079** |
| Plain human (a personal journal entry of mine, not reproduced) | 236 | 12.4 | **0.398** | 0.633 → 0.04 | 0.818 → 0.21 | 0.025 → 1.00 | 0.000 → 0.00 | **0.197** |

The plain human input meets criterion 1's definition of "written plainly": 12.4 words per sentence and 4.19 letters per word.

**What I changed because of it.** The style weights started at spread 0.35, vocabulary 0.25, punctuation 0.25, dash/colon 0.15. With those, the AI texts only reached 0.53–0.55, and plain human writing scored 0.32. Calibration showed:
- **Sentence spread** was the only measure that ranked all four inputs correctly.
- **Vocabulary** (type-token ratio) scored the AI text and my abstract the same, 0.85. It gave no information.
- **Punctuation** scored my plain writing as *more* AI-like than the AI text (0.025 vs 0.072). Moving the anchors can't fix that, because plain human writing sits on the far side of the AI text. It's backwards for exactly the writer criterion 1 protects.

So I moved the weights to **spread 0.60, vocabulary 0.10, punctuation 0.15, dash/colon 0.15**. I kept the weak measures at a small weight instead of dropping them, so a single trick like splitting sentences can't move the whole style score by itself. The anchors and the model signal's midpoint (perplexity 45) are unchanged.

**What the light edit showed.** Changing a few words, adding a typo ("truely"), a paragraph break and an exclamation mark moved the style score by 0.01 and the model score by 0.02. Word-level edits don't change the shape of the text. An edit that rewrote sentence lengths would.

**Limits.** These are four inputs, and two of them are short. The plain human text has typos and unusual phrasing, which raise perplexity and help it read as human to the model signal. A cleanly typed plain text may score higher, and that's the case to watch in unit 8.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** Average the two signals with equal weight. Then apply one rule about disagreement: **the AI label needs both signals to lean AI.** If either signal says the text leans human (scores below 0.5), the combined score is capped just under the AI threshold, so the worst a split can produce is "unsure", never "high-confidence AI". When the two agree, the average stands as it is. (Stretch goal: before the cap, the phrase signal can nudge the average toward AI by up to 20% of the distance left. See *Signal three* above.)

Why equal weights: each signal has a different blind spot. The model signal is fooled by plain, common phrasing, and the style signal by surface edits like splitting sentences. On my calibration inputs neither was more trustworthy than the other, so I had no evidence to favour one.

Why the disagreement rule: a wrong accusation costs a writer much more than a missed detection costs the site. A split means one of the two methods thinks a person wrote it, and that alone is reason not to tell anyone otherwise with confidence. The cost is that AI text which fools just one signal gets "unsure" instead of "AI". I accept that trade.

**The numbers:**

| Setting | Value | In `config.py` |
|---|---|---|
| Model signal weight | 0.5 | `WEIGHT_MODEL_SIGNAL` |
| Style signal weight | 0.5 | `WEIGHT_STYLE_SIGNAL` |
| Phrase signal nudge (stretch) | up to 20% of the distance to 1 | `WEIGHT_PHRASE_SIGNAL` |
| A signal "leans AI" at | 0.5 or above | `SIGNAL_LEANS_AI` |
| Cap when the signals split | 0.64 (`AI_THRESHOLD` − 0.01) | `SPLIT_CAP` |
| High-confidence human | combined score 0.35 or below | `HUMAN_THRESHOLD` |
| High-confidence AI | combined score 0.65 or above | `AI_THRESHOLD` |

Example: model 0.95, style 0.35. A plain average gives 0.65, which is the AI label. Under my rule the style signal leans human, so the score is capped at 0.64, which is unsure.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

Both signals on the same pieces, with the calibrated style weights and my combining rule (an equal-weight average with the split cap; human at 0.35 or below, AI at 0.65 or above). The cap didn't change any of these five scores:

| Piece | Who wrote it | Model | Style | Gap | Combined | Label |
|---|---|---|---|---|---|---|
| Time-management essay | Claude (AI), unedited | 0.887 | 0.718 | 0.17 | 0.842 (0.802 before the phrase signal) | AI |
| Review-hijacking abstract | me, formal | 0.413 | 0.079 | 0.33 | 0.246 | human |
| Journal entry (not reproduced) | me, plain | 0.396 | 0.197 | 0.20 | 0.296 | human |
| "Hi! This is Monika and I'm so glad to be here. I just want to see how this app flags this text." | me, casual | **0.550** | **0.150** | **0.40** | **0.3499** | human, by a hair |
| "Next is step 2 of Milestone 3: read text and creator_id from the request…" (47 words) | Claude (AI) | 0.274 | 0.352 | 0.08 | 0.313 | human (wrong) |

**Where they agree.** On the long pieces they point the same way. Both call the AI essay AI, and both call my abstract and my journal human. The style signal is the more confident of the two on human writing.

**Where they split.** My short casual message is the clearest split. The model signal leans AI (0.550) because "so glad to be here" and "I just want to see how" are friendly, common phrases GPT-2 predicts easily. The style signal says human (0.150) because the sentences vary in length: "Hi!" is next to a 17-word sentence. The placeholder average lands at **0.3499**, one ten-thousandth under the 0.35 human threshold. A ten-thousandth of a point higher and an honest, three-sentence message from me would be told the system is unsure about it.

This is the case my combining rule has to handle. When one signal says AI and the other says human, a plain average turns the disagreement into a number in the middle, and where that number falls is close to arbitrary. The model signal is also the less reliable one on short, friendly text; that's its blind spot. My rule should treat a large gap between the two as uncertainty in its own right, and should never let one signal alone push a split case into the AI band.

**What my rule does with it.** The style signal (0.150) leans human, so this counts as a split and the score is capped at 0.64. Here the average (0.3499) is already well under the cap, so the label stays human. The cap matters for the opposite split: had the model signal said 0.95 on a text the style signal scored 0.35, a plain average would label it AI at 0.65. My rule makes that unsure (0.64).

**Agreeing isn't the same as being right.** The last row is AI text that both signals call human-ish. Technical words (`creator_id`, "README contract") surprise GPT-2, and the three sentences vary in length. No combining rule fixes a case where both signals miss. It's a blind spot they share, and it's a missed AI detection, not a false accusation.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 to 0.35 | "We think this was probably written by a person." |
| unsure | above 0.35 and below 0.65 | "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything." |
| high-confidence AI | 0.65 to 1.00 | "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result." |

The score is the combined score from `scoring.py::combine_signals`. A score of exactly 0.35 counts as human, and exactly 0.65 counts as AI. Because of my combining rule, a text only reaches the AI range when both signals lean AI.

**All three are reachable.** `scoring.label_ranges()` prints `0.00 – 0.35`, `0.35 – 0.65`, `0.65 – 1.00`, with no gap between them. Real submissions through `/submit`:

| Text | Model | Style | Combined | Label |
|---|---|---|---|---|
| Time-management essay (AI) | 0.8867 | 0.7175 | 0.8417 (0.8021 before the phrase signal) | high-confidence AI |
| My review-hijacking abstract | 0.4132 | 0.0785 | 0.2459 | high-confidence human |
| "Hi! This is Monika and I **am** so glad to be here. I just want to see how this app flags this text." | 0.5545 | 0.1659 | 0.3602 | unsure |

The unsure case is the same message as my split case, with "I'm" written as "I am". That one change moved the combined score from 0.3499 (human) to 0.3602 (unsure). Short texts sit close to the boundaries, and a contraction is enough to cross one. That's a good reason the unsure label had to be harmless to receive.

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The person reading it may well have written every word, and my own short message landed right on the edge of this band. So the label does four things, in this order:
- **It says plainly that we don't know.** It doesn't use a hedged half-accusation like "may contain AI content".
- **It names a person first.** "A person or an AI tool" puts the more likely, innocent answer first.
- **It explains why without blaming the writer.** "Mixed patterns" is something about our check, not something they did wrong. Saying this happens with a lot of genuine human writing is true: my plain journal entry and my casual message both scored closer to this band than my formal abstract did.
- **It ends by saying "This is not an accusation" and that they don't need to do anything.** A writer who gets "unsure" on their own work shouldn't feel they have to defend themselves.

It doesn't mention appeals. Offering an appeal for "unsure" would suggest something is wrong that needs fixing. The appeal goes on the AI label, where it's needed.

The AI label is worded with the same care. It says "probably", calls itself "an automated guess, not proof", and names the writers it most often gets wrong (plain, simple writing; see my false-positive trace). It also tells the reader exactly what to do if it's wrong.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Hi! This is Monika and I am so glad to be here. I just want to see how this app flags this text.", "creator_id": "monika"}'
```

```json
{
  "combined_score": 0.3602,
  "confidence": 0.2796,
  "content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a",
  "creator_id": "monika",
  "guess": "unsure",
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "model_score": 0.5545,
  "status": "decided",
  "style_score": 0.1659
}
```


**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a", "reasoning": "I wrote this myself as a quick hello. It is short and casual, which is probably why the checker could not decide."}'
```

```json
{
  "content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a",
  "message": "Thanks for telling us. A person will review this result. Nothing changes automatically in the meantime.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.3602,
      "content_id": "65954d5a-ba08-4a33-a27f-038168a4d547",
      "creator_id": "monika",
      "guess": "unsure",
      "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
      "model_score": 0.5545,
      "status": "decided",
      "style_score": 0.1659,
      "timestamp": "2026-11-03T22:56:30+00:00"
    },
    {
      "combined_score": 0.3602,
      "content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a",
      "creator_id": "monika",
      "guess": "unsure",
      "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
      "model_score": 0.5545,
      "status": "decided",
      "style_score": 0.1659,
      "timestamp": "2026-11-03T22:58:06+00:00"
    },
    {
      "content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a",
      "creator_id": "monika",
      "event": "appeal",
      "reasoning": "I wrote this myself as a quick hello. It is short and casual, which is probably why the checker could not decide.",
      "status": "under_review",
      "timestamp": "2026-11-03T22:58:06+00:00"
    }
  ]
}
```

The last two entries are the submission above and its appeal: same `content_id`, the original decision still `decided` and untouched, and the appeal after it with status `under_review` and the writer's reasoning. The first entry is an earlier run of the same text, from my label tests. Same text, same scores.

**Checking an item's status (stretch goal: `GET /content/<id>`)**

The appealed submission above, looked up by its `content_id`. The status reads `under_review` and the appeal is listed. `phrase_score` is `null` because this item was scored before the phrase signal was added.

```bash
$ curl http://127.0.0.1:5000/content/3f21f8bd-0416-4b3d-b1db-004b3cd42a4a
```

```json
{
  "appeals": [
    {
      "reasoning": "I wrote this myself as a quick hello. It is short and casual, which is probably why the checker could not decide.",
      "timestamp": "2026-11-03T22:58:06+00:00"
    }
  ],
  "combined_score": 0.3602,
  "content_id": "3f21f8bd-0416-4b3d-b1db-004b3cd42a4a",
  "guess": "unsure",
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "model_score": 0.5545,
  "phrase_score": null,
  "status": "under_review",
  "style_score": 0.1659,
  "submitted_at": "2026-11-03T22:58:06+00:00"
}
```

An ID that doesn't exist:

```bash
$ curl http://127.0.0.1:5000/content/not-a-real-id
```

```json
{
  "error": "unknown_content_id",
  "message": "We couldn't find a submission with that ID. Check it matches the one on your result."
}
```

(HTTP 404.)

---

## How I Used AI

I used Claude (in Claude Code) throughout this unit. It explained the assignment steps, drafted most of the README text and wrote most of the code, and I tested, supplied my own writing, and made the decisions about what the service should do. Two moments where what came back changed because of me:

**Moment 1: em dashes and colons**

- *What I asked for:* To implement `punctuation_density`. Once I saw it, I asked for em dashes and colons to count for more, because recent chatbots overuse them.
- *What came back:* First, a measure that counted all the "interesting" marks the same. Then a version where em dashes, en dashes and colons counted double. Claude pointed out a problem with that: the other marks (`?`, `!`, parentheses) lean human while em dashes and colons lean AI, so one number would mix two directions and `style_signal` couldn't tell which had pushed it up.
- *What I changed:* I had it split them. Em dashes, en dashes and colons became a separate fourth measure, `dash_colon_rate`, where higher means more AI. `punctuation_density` now counts only the human-leaning marks. Typed dashes (`-`, `--`) stay with the human marks, since people typing usually use those. The weighting I first asked for was removed.

**Moment 2: calibrating the style signal**

- *What I asked for:* To calibrate the style signal against the four Milestone 4 inputs.
- *What came back:* A `calibrate.py` script and an AI-written essay for the "clearly AI" input. Claude asked me for the other three, because human samples have to be my own writing. Its first weights (spread 0.35, vocabulary 0.25, punctuation 0.25, dash/colon 0.15) turned out wrong on my texts. My plain journal entry scored *more* AI-like on punctuation than the AI essay, and vocabulary scored the AI essay and my abstract the same.
- *What I changed:* I supplied my own paper abstract and a journal entry, and did the light edit of the AI essay myself (a few words, a typo, a paragraph break, an exclamation mark). The weights moved to spread 0.60, vocabulary 0.10, punctuation 0.15, dash/colon 0.15, based on those results. I didn't want `calibrate.py` in the project, so I had it deleted, and the README now records the results instead. My journal entry is personal, so it was scored from a temporary file outside the repo and appears here only as numbers.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
