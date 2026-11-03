"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?
    dash_colon_rate          how often em dashes and colons appear (added)

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

# Window for the moving-average type-token ratio.
TTR_WINDOW = 50

# Punctuation that varies between writers. Full stops are left out. A typed
# dash is a hyphen or double hyphen with a space on at least one side.
PUNCTUATION = re.compile(r"[,;()!?]|(?<=\s)--?|--?(?=\s)")

# Kept apart from PUNCTUATION because they point the other way: recent chat
# models lean on em/en dashes and colons, while people typing on a keyboard
# mostly reach for "-" or "--" instead of "—".
DASH_COLON = re.compile(r"[—–:]")

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. ← TODO

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.

    **My scale:** the coefficient of variation of sentence length in words
    (stdev ÷ mean). 0.0 means every sentence is the same length; prose with
    real variety lands around 0.5 and up. **Higher means more human.**

    **The edge case:** with fewer than two sentences there's no spread to
    measure, so this returns 0.0. That 0.0 means "no evidence", not "AI-like" —
    `style_signal` has to check the sentence count and not read it as even
    rhythm, or every one-sentence submission gets pushed toward AI.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n > 0]   # "!!!" splits as a sentence with no words
    if len(lengths) < 2:
        return 0.0
    return round(statistics.stdev(lengths) / statistics.mean(lengths), 4)


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. ← TODO

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.

    **My fix for the length problem:** a moving-average TTR. Slide a 50-word
    window along the text, take the TTR of each window, and average them. Every
    window is the same size, so a 100-word text and a 1,000-word text are
    measured on the same footing. Under 50 words it falls back to plain TTR
    over the whole text. **Higher means more human.** Empty text returns 0.0.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    if len(tokens) <= TTR_WINDOW:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [
        len(set(tokens[i:i + TTR_WINDOW])) / TTR_WINDOW
        for i in range(len(tokens) - TTR_WINDOW + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length. ← TODO

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.

    **My choice:** count the marks that vary between writers — commas,
    semicolons, parentheses, question marks, exclamation marks and typed dashes
    (" - " or "--") — and leave out full stops, which every sentence has. A
    hyphen inside a word ("well-known") isn't counted. Em dashes, en dashes and
    colons are left out too: they point toward AI, so they get their own
    measure, `dash_colon_rate`. Returned as marks per word, so 0.15 means about
    three marks every twenty words. Empty text returns 0.0.

    **Higher means more human:** sparse, tidy punctuation is what "most likely
    next word" produces.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    return round(len(PUNCTUATION.findall(text)) / len(tokens), 4)


def dash_colon_rate(text: str) -> float:
    """
    Em dashes, en dashes and colons per word. My fourth measure.

    Split out of `punctuation_density` because these marks point the other
    way. Recent chat models lean on "—" for asides and ":" to set up a point,
    while people typing on a keyboard mostly use "-" or "--", which
    `punctuation_density` counts instead. Empty text returns 0.0.

    **Higher means more AI.**

    What it can't see: anyone who writes with real em dashes — some word
    processors and phones turn "--" into "—" automatically, and some writers
    simply like them. Treat it as a nudge, not a verdict.
    """
    tokens = words(text)
    if not tokens:
        return 0.0
    return round(len(DASH_COLON.findall(text)) / len(tokens), 4)


# ── Combining them ───────────────────────────────────────────────────────────

# (human anchor, AI anchor) for each measure. A value at the human anchor
# scores 0, at the AI anchor scores 1. For the first three the human anchor is
# the higher number, which is what flips them.
ANCHORS = {
    "spread": (0.65, 0.25),        # coefficient of variation of sentence length
    "ttr": (0.85, 0.70),           # moving-average type-token ratio
    "punctuation": (0.15, 0.05),   # human-leaning marks per word
    "dash_colon": (0.0, 0.03),     # em/en dashes and colons per word
}

# Set by the Milestone 4 calibration (see README). Spread is the only measure that ranked all four
# calibration inputs the right way round; type-token ratio scored AI and human
# text the same (~0.85), and punctuation scored plain human writing as MORE
# AI-like than the AI text. They keep a small weight rather than none, so a
# single trick (splitting sentences) can't move the whole score on its own.
WEIGHTS = {
    "spread": 0.60,
    "ttr": 0.10,
    "punctuation": 0.15,
    "dash_colon": 0.15,
}

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.

    **How mine works.** Each measure is turned into its own 0–1 "AI-ness" by
    placing it between two anchors in `ANCHORS`: the value I expect from human
    writing scores 0, the value I expect from AI writing scores 1, and anything
    past either end is clamped. Writing the anchors in that order flips the
    measures where higher means human, so every part points the same way. Then
    a weighted average, using `WEIGHTS`.

    The dash and colon rate gets the smallest weight. Plenty of AI text has
    none, so it's a nudge, not a deciding vote.

    **Edge cases.** No words at all scores 0.5: no evidence either way. Fewer
    than two sentences leaves sentence spread out entirely, because its 0.0
    there means "couldn't measure", not "perfectly even" — counting it would
    push every one-sentence submission toward AI.

    The anchors are first guesses. Move them after the calibration inputs, and
    say so in the README.
    """
    if not words(text):
        return 0.5

    measures = {
        "spread": sentence_length_spread(text),
        "ttr": type_token_ratio(text),
        "punctuation": punctuation_density(text),
        "dash_colon": dash_colon_rate(text),
    }
    if len(sentences(text)) < 2:
        del measures["spread"]

    total = sum(WEIGHTS[name] for name in measures)
    score = sum(
        WEIGHTS[name] * _ai_ness(value, *ANCHORS[name])
        for name, value in measures.items()
    ) / total
    return round(score, 4)


def _ai_ness(value: float, human: float, ai: float) -> float:
    """Where `value` sits from the human anchor (0) to the AI anchor (1), clamped."""
    return min(max((value - human) / (ai - human), 0.0), 1.0)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"dash_colon_rate          {dash_colon_rate(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
