"""
Signal three: the phrase signal. ← STRETCH GOAL

Signal one asks how predictable the text is. Signal two measures its shape.
This one reads for specific wording: the stock phrases and favourite words that
chat models fall back on — "It is important to note", "In today's fast-paced
world", "delve", "a testament to".

    python phrases.py "some text to look at"

Why it might differ between human and AI writing: a chat model trained to
sound helpful and polished reaches for the same safe transitions and the same
handful of impressive-sounding words, far more often than people do.

⚠️ **The blind spot.** It only knows the phrases on its list.

  - It's the easiest signal to fool: delete or swap the phrases and it reads 0.
  - The list ages. New models pick up new habits and drop old ones.
  - People use these phrases too. Students are taught "In conclusion" and
    "Additionally", and second-language writers lean on set phrases because
    they know they're correct. Formulaic does not mean machine-written.

That last point is why `scoring.combine_signals` gives it the smallest weight
and no say in the split rule.
"""

import re

import stylometry

# Lower-case patterns, matched on word boundaries. Each match is one hit.
STOCK_PHRASES = [
    r"it is (also )?(important|worth noting|essential|crucial) to",
    r"it's (also )?(important|worth noting|essential|crucial) to",
    r"in today's (fast-paced|digital|modern|ever-changing)",
    r"fast-paced",
    r"ever-(changing|evolving)",
    r"in conclusion",
    r"ultimately,",
    r"additionally,",
    r"furthermore,",
    r"moreover,",
    r"one of the most (important|valuable|significant)",
    r"plays? a (crucial|vital|pivotal|key) role",
    r"in the realm of",
    r"a testament to",
    r"delves?|delving",
    r"tapestry",
    r"navigat(e|es|ing) the",
    r"embark(s|ing)? on",
    r"(rich|complex|intricate) landscape",
    r"harness(es|ing)? the power",
    r"unlock(s|ing)? the",
    r"seamless(ly)?",
    r"multifaceted",
    r"pivotal",
    r"underscores?",
    r"foster(s|ing)?",
    r"by doing so",
    r"not only .{1,60}? but also",
]

_PATTERN = re.compile(r"\b(?:" + "|".join(STOCK_PHRASES) + r")", re.IGNORECASE)

# Hits per 100 words at which the score reaches 1.0. Two stock phrases in every
# hundred words is heavy; the AI essay I calibrated on has about that.
SATURATION_PER_100_WORDS = 2.0


def phrase_hits(text: str) -> list[str]:
    """Every stock phrase found, in order, as it appears in the text."""
    return [m.group(0) for m in _PATTERN.finditer(text)]


def phrase_signal(text: str) -> float:
    """
    Stock phrases per 100 words, scaled to 0–1. **Higher means more AI.**

    0 hits scores 0.0; SATURATION_PER_100_WORDS or more scores 1.0. Empty text
    scores 0.0. A 0.0 here is weak evidence: plenty of AI text uses none of
    these, which is one reason the weight is small.
    """
    n_words = len(stylometry.words(text))
    if not n_words:
        return 0.0
    per_100 = len(phrase_hits(text)) / n_words * 100
    return round(min(per_100 / SATURATION_PER_100_WORDS, 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "In today's fast-paced world, it is important to note that technology "
        "plays a crucial role. Ultimately, it is a testament to human ingenuity."
    )
    hits = phrase_hits(text)
    print(f"{len(stylometry.words(text))} words, {len(hits)} stock phrases")
    for h in hits:
        print(f"  - {h}")
    print(f"\nphrase_signal   {phrase_signal(text)}   (higher = more likely AI)")
