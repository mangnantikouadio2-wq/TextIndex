from pathlib import Path

EXCLUDED = {".venv", "venv", "__pycache__", ".git", "node_modules", "build", ".pytest_cache"}
def index_by_glob(engine, pattern: str) -> None:
    for file_path in engine.folder.rglob(pattern):
        if any(part in EXCLUDED for part in file_path.parts):
            continue
        try:
            text = file_path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"⚠️ Playback impossible: {file_path} {exc}")
            continue
        engine.contents[file_path] = text
        tokens = {w.strip(".,!?\"'();:").lower() for w in text.split()}
        tokens.discard("")
        for token in tokens:
            engine.index.setdefault(token, set()).add(file_path)


def index_text_files(engine) -> None:
    index_by_glob(engine, "*.txt")

def index_markdown_files(engine) -> None:
    index_by_glob(engine, "*.md")

def index_log_files(engine) -> None:
    index_by_glob(engine, "*.log")

def index_csv_files(engine) -> None:
    index_by_glob(engine, "*.csv")