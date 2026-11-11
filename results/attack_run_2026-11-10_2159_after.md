# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-10 21:59
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `98f51fdd-0415-4e5d-8a47-489131dc20d0` | unsure | 0.087 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `4d0d21ce-5e3b-4fd9-b509-79efa812031d` | unsure | 0.106 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `cfac42b8-4ea5-4326-a068-cfb9e59b5ff4` | unsure | 0.173 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `ee0a5d08-8202-456e-85c3-c8f918e7b834` | ai | 0.361 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f9039b93-90f2-4e2c-8666-f77f3268f3ec` | human | 0.468 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `af529689-17ae-434c-92c3-306c641d3a03` | unsure | 0.276 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `17019e6c-5367-46ca-919f-11dbdaaf6a22` | unsure | 0.022 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `5bc13fec-c440-4550-ab81-f9b6726a880e` | unsure | 0.054 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ba4eaf52-77a6-43ec-8edf-d293130ad3fe` | unsure | 0.128 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `b712c451-32a1-4aaf-9b58-28db5fa0be62` | ai | 0.613 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `0efaf732-9ea8-46d2-8d21-2ea368e1685e` | unsure | 0.085 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e1220327-01e9-43ca-a1cd-2190fef5f098` | ai | 0.542 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `41c0acbb-11ca-4aa0-86b7-d541e53bbad2` | ai | 0.458 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `a3bca868-2505-4535-8b47-ca759e248e80` | ai | 0.511 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `ed54439c-402b-445e-8279-88a045ab7fdb` | ai | 0.610 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `537e2dd2-1c13-45eb-9262-80d9812a38e4` | unsure | 0.280 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `e6989fb9-cfad-42dd-8e69-96e7953368a7` | unsure | 0.132 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `568b125b-4fb0-408c-bb63-d5f7ed6079bf` | human | 0.387 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ea84c3a1-2214-4e64-95ac-650558225729` | human | 0.535 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0326b79b-cc5c-4aeb-9f20-bd0acfdd1cf7` | unsure | 0.296 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `a0368a16-f1c1-4b8d-b5ce-3306626654d2` | unsure | 0.013 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `38d82421-64d3-4a4c-87d4-658a492af790` | unsure | 0.133 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `97ae114d-0a51-4031-8fd8-e1cc8f4fbb1e` | unsure | 0.040 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 200 | `fbdc50c2-08bd-449f-87fc-c63e63e639b4` | unsure | 0.280 |  |
| MF06 | malformed | text is emoji only | 200 | `f1d3103f-9f4a-421e-8874-b04cd96b3065` | unsure | 0.280 |  |
| MF07 | malformed | text is right-to-left script | 200 | `7fef2498-5513-48d4-a2f2-59375c0593f9` | unsure | 0.280 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66ef4d1f-a056-4b0e-9f7f-80601f98af25` | human | 0.596 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2a0459b7-8423-4c54-9d28-e59242787734` | human | 0.596 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `25e73697-a558-4595-adeb-d00dfa40dc9a` | human | 0.596 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `208bea97-c73c-4f8e-af3f-5abc771f30fa` | human | 0.596 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e83191ec-c37b-4f74-836a-06090cd846ea` | human | 0.596 |  |
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
  "content_id": "98f51fdd-0415-4e5d-8a47-489131dc20d0",
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
  "content_id": "4d0d21ce-5e3b-4fd9-b509-79efa812031d",
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
  "content_id": "cfac42b8-4ea5-4326-a068-cfb9e59b5ff4",
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
  "content_id": "ee0a5d08-8202-456e-85c3-c8f918e7b834",
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
  "content_id": "f9039b93-90f2-4e2c-8666-f77f3268f3ec",
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
  "content_id": "af529689-17ae-434c-92c3-306c641d3a03",
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
  "content_id": "17019e6c-5367-46ca-919f-11dbdaaf6a22",
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
  "status": 200,
  "content_id": "5bc13fec-c440-4550-ab81-f9b6726a880e",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.054,
  "model_score": 0.2452,
  "style_score": 0.7008,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
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
  "content_id": "ba4eaf52-77a6-43ec-8edf-d293130ad3fe",
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
  "content_id": "b712c451-32a1-4aaf-9b58-28db5fa0be62",
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
  "content_id": "0efaf732-9ea8-46d2-8d21-2ea368e1685e",
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
  "content_id": "e1220327-01e9-43ca-a1cd-2190fef5f098",
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
  "content_id": "41c0acbb-11ca-4aa0-86b7-d541e53bbad2",
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
  "content_id": "a3bca868-2505-4535-8b47-ca759e248e80",
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
  "content_id": "ed54439c-402b-445e-8279-88a045ab7fdb",
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
  "content_id": "537e2dd2-1c13-45eb-9262-80d9812a38e4",
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
  "content_id": "e6989fb9-cfad-42dd-8e69-96e7953368a7",
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
  "content_id": "568b125b-4fb0-408c-bb63-d5f7ed6079bf",
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
  "content_id": "ea84c3a1-2214-4e64-95ac-650558225729",
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
  "content_id": "0326b79b-cc5c-4aeb-9f20-bd0acfdd1cf7",
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
  "content_id": "a0368a16-f1c1-4b8d-b5ce-3306626654d2",
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
  "status": 200,
  "content_id": "38d82421-64d3-4a4c-87d4-658a492af790",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.133,
  "model_score": 0.6401,
  "style_score": 0.4929,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
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
  "content_id": "97ae114d-0a51-4031-8fd8-e1cc8f4fbb1e",
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
  "status": 200,
  "content_id": "fbdc50c2-08bd-449f-87fc-c63e63e639b4",
  "creator_id": "attacker_MF05",
  "guess": "unsure",
  "confidence": 0.28,
  "model_score": 0.9976,
  "style_score": 0.375,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "f1d3103f-9f4a-421e-8874-b04cd96b3065",
  "creator_id": "attacker_MF06",
  "guess": "unsure",
  "confidence": 0.28,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "7fef2498-5513-48d4-a2f2-59375c0593f9",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.28,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We can't tell whether a person or an AI tool wrote this. The patterns we look for were mixed, and that happens with a lot of genuine human writing. This is not an accusation. If you wrote it yourself, you don't need to do anything.",
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
  "status": 200,
  "content_id": "66ef4d1f-a056-4b0e-9f7f-80601f98af25",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5962,
  "model_score": 0.0287,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "2a0459b7-8423-4c54-9d28-e59242787734",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5962,
  "model_score": 0.0287,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "25e73697-a558-4595-adeb-d00dfa40dc9a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5962,
  "model_score": 0.0287,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "208bea97-c73c-4f8e-af3f-5abc771f30fa",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5962,
  "model_score": 0.0287,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e83191ec-c37b-4f74-836a-06090cd846ea",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.5962,
  "model_score": 0.0287,
  "style_score": 0.375,
  "label": "We think this was probably written by a person.",
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
