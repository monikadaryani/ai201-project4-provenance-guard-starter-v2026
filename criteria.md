# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. False positives: my own writing is not called AI

Of 10 pieces I wrote myself, at least 4 of them written plainly, **at most 1** gets the high-confidence AI label. This has to hold in **each** of the three trials, not on average.

**"Written plainly" means both of these are true for the piece**, measured with the `sentences()` and `words()` helpers in `stylometry.py`:
- **Average sentence length is 14 words or fewer** (number of words ÷ number of sentences).
- **Average word length is 4.5 letters or fewer** (total letters in all words ÷ number of words).

Each piece is at least 5 sentences long, and I check the two numbers before it goes in `scenarios.py`, so whether a piece counts as plain is decided before I see its score.

**Why this target:** A wrong accusation is the expensive mistake. It costs a real writer their reputation, while a missed piece of AI text costs the site a little. My false-positive trace showed that plain, careful writing is exactly what both signals read as AI, so I'm loading the test with that kind of writing on purpose instead of my most "human-sounding" work. One in ten is still a real person accused, so it's the most I'll accept, and it has to hold every time because the model signal can score the same text differently on different runs.

---

## 2. Score spread: AI and human text land clearly apart

Across 5 clearly AI-generated texts and 5 clearly human-written texts, the average `combined_score` of the AI group is **at least 0.30 higher** than the average of the human group, in each of the three trials.

**Why this target:** If the two groups score close together, the labels are a coin toss with a confident voice. 0.30 is the width of my "unsure" band (0.35 to 0.65), so a gap that size means the clear cases sit on opposite sides of it instead of piling up in the middle. If I can't get that much separation on the easy cases, the thresholds have nothing to stand on.

---

## 3. Label coverage: all three labels are reachable

Out of 9 inputs (3 I expect to read as human, 3 borderline, 3 I expect to read as AI), **each of the three labels is produced at least once**, in each of the three trials.

**Why this target:** A label nobody can reach is a gap in my score ranges, and a reader would never see it. The unsure label matters most here: it's where honest writers who happen to write plainly should land instead of being accused. If borderline text never produces it, my thresholds are pushing everyone to one side.

---

## 4. The appeal path: every appeal is recorded and changes status

For **5 of 5** appeals on real `content_id`s, the response is 200 with `status: "under_review"`, the log gains exactly one appeal entry for that ID, and the original decision entry is still there unchanged. An appeal on a made-up `content_id` returns **404** with `unknown_content_id` in 1 of 1 tries.

**Why this target:** The appeal is the only thing between a wrong accusation and nothing at all, so "usually works" isn't good enough. It has to work every time. The made-up ID check matters because an appeal that fails silently looks to the writer like it went through when it didn't. The original decision has to stay in the log so anyone reviewing can see what was decided and that it was challenged.

---

## 5. Bad input: malformed requests get a clear error, not a crash

Of 6 malformed `/submit` requests (empty text, whitespace-only text, missing `text` field, `text` set to null, `text` set to a number, and a 50,000-word text), **6 of 6** return a 4xx status with an `error` field, **0** return a 5xx, and `/ping` still answers afterwards. This has to hold in each of the three trials.

**Why this target:** A crash on bad input is one of the most common real failures, and unit 8's attack set will send exactly these. A 500 tells the caller nothing and counts as BROKE in `run_attacks.py`. The error codes have to match the contract in my README, so a client can tell "your text is empty" apart from "the service is down". Checking `/ping` afterwards confirms one bad request didn't take the whole service down.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
