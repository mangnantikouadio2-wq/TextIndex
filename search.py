from pathlib import Path

def search_and(self, *words: str) -> set[Path]:
    sets = [self.index.get(w.lower(), set()) for w in words]
    return set.intersection(*sets) if sets else set()

def search_or(self, *words: str) -> set[Path]:
    sets = [self.index.get(w.lower(), set()) for w in words]
    return set.union(*sets) if sets else set()

def search_not(self, *words: str) -> set[Path]:
    sets = [self.index.get(w.lower(), set()) for w in words]
    return set.difference(*sets) if sets else set()