# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 22:20
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `6193c9e4-1017-483f-99ad-25fa83241780` | unsure | 0.087 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `ce3e6e23-d58d-4714-b2d0-cb7245d9971b` | unsure | 0.106 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4b0a17ec-9da1-4006-b640-6fcca8b9cecc` | unsure | 0.173 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `cdc53ee0-33ad-426e-b083-d4302d1633cb` | ai | 0.361 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `eba970da-1c74-409f-9569-26935ef91ccd` | human | 0.468 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e74b98a6-1650-4e1b-9b35-9c14ee8b786a` | unsure | 0.276 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ce2d05bf-9237-4cfc-84b4-99d5166d19fe` | unsure | 0.022 |  |
| EV08 | evasion | signal one: text below the token window | 400 | `—` | — | — |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `148adb67-3a70-41d7-8031-0c96dc6a7174` | unsure | 0.128 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `6412d7d2-68d0-415c-bac9-f1af2941fe89` | ai | 0.613 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `4a8df56c-1d5f-40e4-a545-965ad48bc0da` | unsure | 0.085 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `1ed92ac0-73f1-40ac-acea-8cd6a2e7c10d` | ai | 0.542 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c91fe9dc-3ecf-4b15-9576-9a447b53cce8` | ai | 0.458 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `cfcc883c-8753-4e84-b658-f8b6821a9e77` | ai | 0.511 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `f9e02aeb-808a-4b88-b82a-f54da23f8b1a` | ai | 0.610 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `60784a6e-0f62-40db-b0d8-d7df8f391b93` | unsure | 0.280 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f1003085-8b9f-4dfd-92ca-016ea8154839` | unsure | 0.132 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `425025fb-7a81-423c-a152-496be22efac3` | human | 0.387 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `86a67bb0-c397-45cd-9934-45536662e3f1` | human | 0.535 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `2c99b6e4-3fba-4688-a4c2-9ce077b67a03` | unsure | 0.296 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `4cba54bc-14c5-4188-994f-5869a1a77958` | unsure | 0.013 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 400 | `—` | — | — |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `86c3e8a7-efa4-41b9-921d-f7db9ee28af8` | unsure | 0.040 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "6193c9e4-1017-483f-99ad-25fa83241780",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.0866,
  "model_score": 0.1635,
  "style_score": 0.75,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "ce3e6e23-d58d-4714-b2d0-cb7245d9971b",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.1056,
  "model_score": 0.5943,
  "style_score": 0.3,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "4b0a17ec-9da1-4006-b640-6fcca8b9cecc",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.1732,
  "model_score": 0.6662,
  "style_score": 0.5069,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "cdc53ee0-33ad-426e-b083-d4302d1633cb",
  "creator_id": "attacker_EV04",
  "guess": "ai",
  "confidence": 0.3614,
  "model_score": 0.6114,
  "style_score": 0.75,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "eba970da-1c74-409f-9569-26935ef91ccd",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.4678,
  "model_score": 0.3212,
  "style_score": 0.211,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "e74b98a6-1650-4e1b-9b35-9c14ee8b786a",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.2764,
  "model_score": 0.5727,
  "style_score": 0.1508,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "ce2d05bf-9237-4cfc-84b4-99d5166d19fe",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.022,
  "model_score": 0.5862,
  "style_score": 0.1364,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "148adb67-3a70-41d7-8031-0c96dc6a7174",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.128,
  "model_score": 0.7042,
  "style_score": 0.4237,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "6412d7d2-68d0-415c-bac9-f1af2941fe89",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.6132,
  "model_score": 0.9792,
  "style_score": 0.6341,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "4a8df56c-1d5f-40e4-a545-965ad48bc0da",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.0854,
  "model_score": 0.6175,
  "style_score": 0.4679,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "1ed92ac0-73f1-40ac-acea-8cd6a2e7c10d",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.5424,
  "model_score": 0.7387,
  "style_score": 0.8036,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "c91fe9dc-3ecf-4b15-9576-9a447b53cce8",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.4582,
  "model_score": 0.8051,
  "style_score": 0.6531,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "cfcc883c-8753-4e84-b658-f8b6821a9e77",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.5114,
  "model_score": 0.8329,
  "style_score": 0.5942,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "f9e02aeb-808a-4b88-b82a-f54da23f8b1a",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.6102,
  "model_score": 0.8005,
  "style_score": 0.8096,
  "label": "We think this was probably written with the help of an AI tool. This is an automated guess, not proof, and it can be wrong, especially for writing that is simple or plain. If you wrote this yourself, you can ask a person to review it using the ID shown with this result.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "60784a6e-0f62-40db-b0d8-d7df8f391b93",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.28,
  "model_score": 0.8814,
  "style_score": 0.4089,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "f1003085-8b9f-4dfd-92ca-016ea8154839",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.1316,
  "model_score": 0.8816,
  "style_score": 0.25,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "425025fb-7a81-423c-a152-496be22efac3",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3874,
  "model_score": 0.4625,
  "style_score": 0.15,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "86a67bb0-c397-45cd-9934-45536662e3f1",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.5346,
  "model_score": 0.2044,
  "style_score": 0.261,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "2c99b6e4-3fba-4688-a4c2-9ce077b67a03",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.2956,
  "model_score": 0.5943,
  "style_score": 0.7013,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "4cba54bc-14c5-4188-994f-5869a1a77958",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0128,
  "model_score": 0.4998,
  "style_score": 0.4873,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_PI05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "86c3e8a7-efa4-41b9-921d-f7db9ee28af8",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.0402,
  "model_score": 0.5583,
  "style_score": 0.4819,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
