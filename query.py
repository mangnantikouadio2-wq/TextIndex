from pathlib import Path

OPERATORS = ["AND", "OR", "NOT"]

def search_and(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.intersection(*sets) if sets else set()

def search_or(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.union(*sets) if sets else set()

def files_with_any(engine, *words: str) -> set[Path]:
    if not words:
        return set()
    excluded: set[Path] = set()
    for w in words:
        excluded |= engine.index.get(w.lower(), set())
    return excluded

def tokenize(query: str) -> tuple[list[tuple[str, list[str]]], list[str]]:
    tokens = query.split()
    if not tokens:
        return [], []
    groups: list[tuple[str, list[str]]] = []
    all_words: list[str] = []
    operator = "OR"
    words: list[str] = []
    for token in tokens:
        if token.upper() in OPERATORS:
            if words:
                groups.append((operator, words))
                words = []
                operator = token.upper()
        else:
            words.append(token)
            all_words.append(token)
    if words:
        groups.append((operator, words))
    return (groups, all_words)

def evaluate(engine, query: str) -> set[Path]:
    groups, _ = tokenize(query)
    if not groups:
        return set()
    result: set[Path] = set()
    for operator, group_word in groups:
        if operator == "AND":
            sub_result = search_and(engine, *group_word)
            result &= sub_result
        elif operator == "OR":
            sub_result = search_or(engine, *group_word)
            result |= sub_result
        elif operator == "NOT":
            sub_result = files_with_any(engine, *group_word)
            result -= sub_result
    return result

def snippet(engine, path: Path, query: str, maxlen: int = 120) -> str:
    _, words = tokenize(query)
    text = engine.contents.get(path, "")
    if not text:
        return "(empty content)"
    lowered = text.lower()
    for w in words:
        pos = lowered.find(w.lower())
        if pos != -1:
            start = max(0, pos -30)
            end = min(len(text), pos + len(w) + maxlen)
            excerpt = text[start:end].replace("\n", " ").strip()
            return ("..." if start > 0 else "") + excerpt + ("..." if end < len(text) else "")
    for line in text.splitlines():
        if line.strip():
            return line.strip()[:maxlen]
    return "(empty)"