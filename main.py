from pathlib import Path
import time
from mini_search_engine import MiniSearchEngine
import query

HELP = """
Commandes:
    :help                       Display this help
    :reload                     Re-index the current directory
    :exit / exit                exit the program

Search synthaxes:
    word1 AND word2            -> the two words
    word1 OR word2             -> at least one word
    word1 NOT word2            -> word1 whithour word2
    Ex : python AND descriptors NOT
"""

def results_format(results: set[Path], engine: MiniSearchEngine, root: Path) -> None:
    if not results:
        print("❌ No result found.")
        return
    print(f"\n📄 {len(results)} file(s) found\n")
    for path in sorted(results):
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        print(f"    ·{path.name} ({rel})")
        print()

def repl(folder: Path) -> None:
    engine = MiniSearchEngine(folder)
    print(f"Found: {len(engine.contents)} files in {folder}")
    print("type :help for help.\n")
    while True:
        request = input("Search > ")
        if not request: continue
        if request in (":exit", "quit", "q"):
            break
        if request == ":help":
            print(HELP)
            continue
        start = time.perf_counter()
        results = query.evaluate(engine, request)
        elapsed = (time.perf_counter() - start) * 1000 
        results_format(results, engine, folder)

if __name__ == "__main__":
    target = Path(input("Folder to scrapp > "))
    repl(target)