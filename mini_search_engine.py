from pathlib import Path
import files
import query

class MiniSearchEngine:
    def __init__(self, folder_path):
        self.folder = Path(folder_path)
        self.index: dict[str, set[Path]] = {}
        self.contents: dict[Path, str] = {}
        files.index_text_files(self)
        files.index_markdown_files(self)
        files.index_log_files(self)
        files.index_csv_files(self)

    def search(self, word: str) -> set[Path]:
        return self.index.get(word.lower(), set())

    
if __name__ == "__main__":
    engine = MiniSearchEngine("/home/mangnanti/Programmation/Audits")
    print(f"Fichiers indexés: {len(engine.contents)}")
    print(f"Mots distincts: {len(engine.index)}")
    request = "your and project and malloc"
    result = query.evaluate(engine, request)
    print("Fichiers trouvés:", [f.name for f in result])    