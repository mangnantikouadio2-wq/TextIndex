from pathlib import Path

def index_by_glob(engine, pattern: str) -> None:
    for file_path in engine.folder.rglob(pattern):
        try:
            text = file_path.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"⚠️ Playback impossible: {file_path} {exc}")
            continue
        engine.contents[file_path] = text
        tokens = {w.strip(".,!?\"'();:") for w in text.split()}
        for token in tokens:
            if token not in engine.index:
                engine.index[token] = set()
            engine.index[token].add(file_path)


def index_text_files(engine) -> None:
    index_by_glob(engine, "*.txt")

def index_markdown_files(engine) -> None:
    index_by_glob(engine, "*.md")

def index_log_files(engine) -> None:
    index_by_glob(engine, "*.log")

def index_csv_files(engine) -> None:
    index_by_glob(engine, "*.csv")