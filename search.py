from pathlib import Path

def search_and(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.intersection(*sets) if sets else set()

def search_or(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.union(*sets) if sets else set()

def search_not(engine, *words: str) -> set[Path]:
    sets = [engine.index.get(w.lower(), set()) for w in words]
    return set.difference(*sets) if sets else set()