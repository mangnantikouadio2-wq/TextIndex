# TextIndex - Mini Full-Text Search Engine in CLI

The objective is to write a standalone Python script that explores a target directory of text files,
builds an in-memory optimized data structure (inverted index), and then provides an
interactive command-line interface for performing complex queries in real time.

## 📋 Requirements

1. Directory indexing

<ul>
    <li>
        <strong>Input</strong>: Path to a directory passed as a parameter (or requested from the user).
    </li>
    <li>
        <strong>Target files</strong>: Analyze all text files (.txt, .md, .log).
    </li>
    <li>
        <strong>Text processing</strong>:
        <ul>
            <li>Case normalization (case-insensitive).</li>
            <li>Basic punctuation cleaning.</li>
            <li>Extraction of unique words per document.</li>
        </ul>
    </li>
    <li>
        <strong>Structure</strong>: Build an in-memory inverted index (mapping a word \rightarrow a set of files).
    </li>
</ul>

2. Query Engine (Boolean Search)

The engine must read a search string entered in the terminal and return the list of matching files.

<ul>
    <li><strong>Simple search</strong>: A single word (e.g., python).</li>
    <li><strong>AND operator</strong>: Words that must all be present (e.g., python AND script).</li>
    <li><strong>OR operator</strong>: Files containing at least one of the words (e.g., bug OR error).</li>
    <li><strong>NOT operator</strong>: Exclude files containing a term (e.g., python NOT django).</li>
    <li><strong>Combinations</strong>: Ability to combine operators in the same query (e.g., python AND data NOT legacy).</li>
</ul>

3. Result Display & Snippets

For each file matching the search:

<ul>
    <li>Display the file name and its relative path.</li>
    <li>
        Display a contextual snippet: the first
        line (or sentence) of the file where one of the searched words appears.
    </li>
    <li>
        Display the total number of documents found and the
        time taken to execute the query (in ms).
    </li>
</ul>

4. Terminal Interface (REPL)

<ul>
    <li>An interactive loop that waits for user input (Search > ).</li>
    <li>A help command (e.g., :help).</li>
    <li>A command to re-index the directory while running without restarting the script (e.g., :reload).</li>
    <li>An exit command (e.g., :quit or exit).</li>
</ul>

## ⚙️ Development Constraints

<ul>
    <li><strong>Dependencies</strong>: Python standard library only (3.10+ recommended).</li>
    <li>
        <strong>Robustness</strong>: Proper handling of I/O errors (unreadable file,
        invalid UTF-8 encoding, nonexistent directory).
    </li>
    <li>
        <strong>Pylint / Pythonic Check</strong>: Use type hints throughout, maintain a clean
        class/method structure, and clearly separate indexing logic from the CLI interface.
    </li>
</ul>
