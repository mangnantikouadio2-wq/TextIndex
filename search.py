from pathlib import Path

def search_and(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.intersection(*sets) if sets else set()

def search_or(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.union(*sets) if sets else set()

def search_not(engine, *words: str) -> set[Path]:
    if not words:
        return set()
    first = engine.index.get(words[0].lower(), set())
    excluded: set[Path] = set()
    for w in words[1:]:
        excluded |= engine.index.get(w.lower(), set())
    return first - excluded