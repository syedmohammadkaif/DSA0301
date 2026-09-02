"""
Component 1: Regex-based text normalisation & tokenization
Component 2: Rule-based (finite-state / morphological) POS tagger
"""
import re

TOKEN_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?|[!?.]")

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"[^a-z0-9!?.'\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text: str):
    return TOKEN_RE.findall(clean_text(text))


# --- Rule-based POS tagger -------------------------------------------------
# Small closed-class lexicon (function words) + suffix/morphology rules for
# open classes. This implements CO3 (rule-based morphology/syntax component).

DETERMINERS = {"the", "a", "an", "this", "that", "these", "those"}
PRONOUNS = {"i", "you", "he", "she", "it", "we", "they", "me", "everyone"}
PREPOSITIONS = {"in", "on", "at", "for", "with", "of", "to", "from", "after", "than"}
CONJUNCTIONS = {"and", "but", "or", "though"}
MODALS = {"would", "will", "must", "could", "can"}
INTENSIFIERS = {"so", "very", "absolutely", "highly", "super", "just"}

ADV_SUFFIXES = ("ly",)
VERB_SUFFIXES = ("ed", "ing", "es")
ADJ_SUFFIXES = ("ful", "ive", "able", "less", "est", "er")
NOUN_SUFFIXES = ("tion", "ness", "ment", "ity", "s")

def tag_token(tok: str) -> str:
    low = tok.lower()
    if tok in "!?.":
        return "PUNCT"
    if low in DETERMINERS:
        return "DET"
    if low in PRONOUNS:
        return "PRON"
    if low in PREPOSITIONS:
        return "PREP"
    if low in CONJUNCTIONS:
        return "CONJ"
    if low in MODALS:
        return "MODAL"
    if low in INTENSIFIERS:
        return "INTENS"
    if low.endswith(ADV_SUFFIXES):
        return "ADV"
    if low.endswith(ADJ_SUFFIXES):
        return "ADJ"
    if low.endswith(VERB_SUFFIXES):
        return "VERB"
    if low.endswith(NOUN_SUFFIXES):
        return "NOUN"
    return "NOUN"  # default open-class fallback

def pos_tag(tokens):
    return [(t, tag_token(t)) for t in tokens]


if __name__ == "__main__":
    s = "This blender is absolutely amazing!!! Best purchase ever!!!"
    toks = tokenize(s)
    print(toks)
    print(pos_tag(toks))
