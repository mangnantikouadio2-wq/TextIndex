def index_text_files(self) -> None:
    for file_path in self.folder.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8").lower()
        tokens = {word.strip(".,!?\"'()") for word in text.split()}
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(file_path)

def index_markdown_files(self) -> None:
    for file_path in self.folder.glob("*.md"):
        text = file_path.read_text(encoding="utf-8").lower()
        tokens = {word.strip(".,!?\"'()") for word in text.split()}
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(file_path)

def index_log_files(self) -> None:
    for file_path in self.folder.glob("*.log"):
        text = file_path.read_text(encoding="utf-8").lower()
        tokens = {word.strip(".,!?\"'()") for word in text.split()}
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(file_path)

def index_csv_files(self) -> None:
    for file_path in self.folder.glob("*.csv"):
        text = file_path.read_text(encoding="utf-8").lower()
        tokens = {word.strip(".,!?\"'()") for word in text.split()}
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(file_path)

def index_odt_files(self) -> None:
    for file_path in self.folder.glob("*.odt"):
        text = file_path.read_text(encoding="utf-8").lower()
        tokens = {word.strip(".,!?\"'()") for word in text.split()}
        for token in tokens:
            if token not in self.index:
                self.index[token] = set()
            self.index[token].add(file_path)