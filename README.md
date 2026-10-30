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

**2. The submission is unpacked and given an ID (`submit()` in `app.py`).** The handler takes `text` and `creator_id` out of the dictionary and checks that the text is actually there. If it's missing or empty, the request is turned away with an error here rather than crashing a later step. It then creates a `content_id` with `uuid.uuid4()`. **It adds** a unique ID for this one submission. Every later step, the log entry, and any appeal the writer files will use this ID to refer to it.

**3. The model signal (`detector.model_signal` in `detector.py`).** The text is run through GPT-2 on the local machine to measure its perplexity, meaning how predictable the model finds each next word. That perplexity is squashed onto a 0–1 scale, where low perplexity means a high score. **It adds** `model_score`, a number from 0 to 1 where higher means "reads more like AI." This step judges the words themselves, not the shape of the text.

**4. The style signal (`stylometry.style_signal` in `stylometry.py`).** The same text is measured as shape only, without reading its meaning. It looks at how much sentence lengths vary, how often vocabulary repeats, and how much punctuation there is and how varied it is. Those three measures are scaled and combined into one number. **It adds** `style_score`, a second 0–1 score where higher means "more like AI." It comes from a completely different kind of evidence than step 3.

**5. The two signals are combined (`scoring.combine_signals` in `scoring.py`).** The two scores are merged into one using the combining rule described under *Signals and Scoring* below. This is also where the service decides what to do when the two signals disagree. **It adds** `combined_score`, one number from 0 (confidently human) to 1 (confidently AI). Every later decision is based on this number.

**6. The score becomes words (`scoring.score_to_label` in `scoring.py`).** The combined score is compared against two thresholds in `config.py`, `HUMAN_THRESHOLD` and `AI_THRESHOLD`. The comparison puts it in one of three bands: high-confidence human, unsure, or high-confidence AI. **It adds** a `guess` (`human` / `unsure` / `ai`) for the machine and a `label`, which is the plain-language sentence a reader actually sees in place of a number.

**7. The decision is logged and returned (`audit.log_decision` in `audit.py`, then the JSON response).** The service writes one line to the append-only audit log. That line holds the timestamp, `content_id`, `creator_id`, both signal scores, the combined score, the guess, the label, and the status `decided`. It then sends the same information back to the caller as JSON. **It adds** a permanent record of the decision that can be checked later and that `/appeal` can find by `content_id`. The response also delivers the label to the reader, which is the end of the path.

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

### The two endpoints

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

**What it measures:** The *shape* of the text, without reading what it says. `stylometry.py` combines three measures into one 0–1 score where higher means more AI-like:
- **Sentence length spread:** do sentence lengths vary, or are they all about the same?
- **Type-token ratio:** what fraction of the words are distinct, or how much the vocabulary repeats.
- **Punctuation density:** how much punctuation there is, and how varied it is.

**Why that might differ between human and AI writing:** Generated prose tends toward even, medium-length sentences, a narrower vocabulary, and tidy, standard punctuation, because "most likely next word" produces average-shaped text. Human writing is lumpier: a three-word sentence next to a forty-word one, a favorite word repeated, a dash or parenthesis or exclamation mark where it feels right. Published linguistic comparisons back this up: human texts show more variation in sentence length and sentence structure, while AI output leans formal and evenly structured, with more dense, noun-heavy phrasing.

**What it can't see:** Meaning. This signal cannot read. It has no idea what the text says or who wrote it, so anything that changes the shape without changing the substance moves the score. Examples are adding typos, splitting or merging sentences, adding dashes and semicolons, or pasting in a quotation. That makes it cheap to fool on purpose: lightly editing AI text this way can push it toward "human." It also misjudges people whose natural style is even and tidy, such as a careful writer following a style guide or someone writing a short, structured answer. Their text has the regular shape this signal reads as AI-like. Short texts are another weak point, because with only a few sentences the three measures are mostly noise. The popular rule that "quirks and flaws mean human" is exactly this weakness. It rewards anyone who adds a few typos, and it penalizes the careful human writer who fixed theirs. Finally, a lot of what really separates human writing is out of reach for both signals because it depends on meaning: emotional depth, sarcasm, a specific remembered detail, an unresolved thought, or whether the reasoning holds up.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

**The numbers:**

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



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
  "combined_score": null,
  "confidence": 0.0,
  "content_id": "ea344e42-3540-44f0-9026-156c3673a599",
  "creator_id": "monika",
  "guess": "unsure",
  "label": "PLACEHOLDER label",
  "model_score": 0.5545,
  "status": "decided",
  "style_score": null
}
```

<!-- Milestone 3 run: only the model signal is wired in. style_score and
     combined_score are null and guess/label/confidence are placeholders until
     Milestones 4 and 5 — re-run and replace this once they're built. -->



**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": null,
      "content_id": "61f9d0a1-4cc4-485a-b514-13eb3b8aff61",
      "creator_id": "monika",
      "guess": "unsure",
      "label": "PLACEHOLDER label",
      "model_score": 0.5545,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-30T21:01:51+00:00"
    },
    {
      "combined_score": null,
      "content_id": "ea344e42-3540-44f0-9026-156c3673a599",
      "creator_id": "monika",
      "guess": "unsure",
      "label": "PLACEHOLDER label",
      "model_score": 0.5545,
      "status": "decided",
      "style_score": null,
      "timestamp": "2026-10-30T21:03:33+00:00"
    }
  ]
}
```

<!-- Milestone 3 run, before /appeal exists. The second entry is the
     submission above (same content_id). Re-run after the appeal so this
     shows the decision followed by its under_review entry. -->

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

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
