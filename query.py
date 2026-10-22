from pathlib import Path

OPERATORS = ["AND", "OR", "NOT"]

def search_and(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.intersection(*sets) if sets else set()

def search_or(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.union(*sets) if sets else set()

def search_not(engine, *words: str) -> set[Path]:
    if not words:
        return set()
    excluded: set[Path] = set()
    for w in words:
        excluded |= engine.index.get(w.lower(), set())
    return excluded

def evaluate(engine, query: str) -> set[Path]:
    tokens = query.split()
    if not tokens:
        return set()
    groups: list[tuple[str, list[str]]] = []
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
    if words:
        groups.append((operator, words))
    result: set[Path] = set()
    for operator, group_word in groups:
        if operator == "AND":
            sub_result = search_and(engine, *group_word)
            result &= sub_result
        elif operator == "OR":
            sub_result = search_or(engine, *group_word)
            result |= sub_result
        elif operator == "NOT":
            sub_result = search_not(engine, *group_word)
            result -= sub_result
    return result