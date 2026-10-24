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

def results_format(results: set[Path], engine: MiniSearchEngine, query_str: str, elapsed_ms: float, root: Path) -> None:
    if not results:
        print("❌ No result found.")
        return
    print(f"\n📄 {len(results)} file(s) found in {elapsed_ms:.2f} ms\n")
    for path in sorted(results):
        rel = path.relative_to(root) if path.is_relative_to(root) else path
        extract = query.snippet(engine, path, query_str)
        print(f"    ·{path.name} ({rel})")
        print(f"       ↳{extract}")
        print()

def repl(folder: Path) -> None:
    engine = MiniSearchEngine(folder)
    print(f"Found: {len(engine.contents)} files in {folder}")
    print("type :help for help.\n")
    while True:
        request = input("Search > ")
        if not request: continue
        if request in (":exit", ":quit", ":q"):
            break
        if request == ":help":
            print(HELP)
            continue
        if request == ":reload":
            engine.reload()
            print(f"♻️ Re-indexed: {len(engine.contents)}")
            continue
        start = time.perf_counter()
        results = query.evaluate(engine, request)
        elapsed = (time.perf_counter() - start) * 1000 
        results_format(results, engine, request, elapsed, folder)

if __name__ == "__main__":
    target = Path(input("Folder to scrapp > "))
    repl(target)