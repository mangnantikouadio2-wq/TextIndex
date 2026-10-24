# TextIndex

> A lightweight, local search engine for personal notes, documentation, and source files.

TextIndex is a small Python command-line tool designed to solve a simple but increasingly frustrating problem: <strong>finding information you know you wrote somewhere, without remembering where you saved it.</strong>

Instead of manually opening dozens or hundreds of Markdown and text files, TextIndex builds an in-memory inverted index and lets you search across an entire directory using keywords and Boolean operators.

No external dependencies. No remote service. Just Python and your own files.

## The Story Behind the Project

I take a lot of notes.

Technical documentation, programming lessons, personal research, project audits, and random ideas all end up somewhere in my collection of Markdown and text files. Over time, finding a particular piece of information became a problem of its own.

I would remember reading or writing something, but not where I had put it. My only option was often to open files one by one and search manually.

What started as a small personal utility also became an opportunity to practise Python, explore data structures, define software contracts, and make architectural decisions around a real-world problem.

## Features

- Recursive directory indexing: search through files within a directory tree.
- Inverted index: map terms to the documents containing them.
- Case-insensitive keyword search: find words regardless of capitalization.
- Boolean queries: combine search terms using "AND", "OR", and "NOT".
- Contextual snippets: inspect a portion of a matching document without opening it manually.
- Relative file paths: identify where a result was found within the indexed directory.
- Interactive command-line interface: execute multiple searches in one session.
- Index reloading: refresh the index when documents change.
- Execution feedback: inspect search results and timing information.
- Directory exclusions: avoid indexing irrelevant folders such as ".git", caches, and virtual environments.

## How It Works

TextIndex relies on two central data structures:

- An inverted index mapping each normalized term to a set of document paths.
- A content store mapping document paths to their text.

Conceptually, an index may look like this:

```text
{
"python": {
"notes/python.md",
"audits/malloc.txt"
},
"pointers": {
"courses/c.md",
"notes/memory.md"
}
}
```

When a query is evaluated, the engine retrieves the relevant document sets and combines them according to the requested Boolean operations.

For example:

`python AND pointers`

returns documents containing both terms, while:

`python OR pointers`

returns documents containing either term.

This approach avoids rereading every file for each individual search. The index is currently held in memory, so the directory must be indexed again when a new session starts.

## Requirements

- Python 3.10 or later.
- No third-party Python packages required.

## Installation

Clone the repository:

```text
git clone git@github.com:mangnantikouadio2-wq/TextIndex.git
cd TextIndex
```

Run the application using the project's entry point:

`python3 main.py`

Follow the interactive prompt to select the directory to index and start searching.

## Optional: Install as a Local Command

TextIndex can also be exposed as a shell command, such as "textindex", using a small launcher in "/usr/local/bin".

The launcher must point to the actual project location and preserve access to its Python modules. This is a local installation convenience, not a requirement for running the application.

## Usage

Start TextIndex:

`python3 main.py`

Choose the directory containing the documents you want to search. Once indexing is complete, use the interactive prompt to enter queries and the supported commands.

Boolean Search

| Operator | Meaning                                |
| :------- | :------------------------------------- |
| "AND"    | Match documents containing both terms  |
| "OR"     | Match documents containing either term |
| "NOT"    | Exclude documents matching a term      |

Examples:

```text
python AND pointers
python OR cybersecurity
python NOT django
```

The exact interpretation of compound queries depends on the query grammar implemented by the current version. Parentheses, operator precedence, and malformed expressions should not be assumed to work unless explicitly supported.

## Interactive Commands

The interactive interface provides commands for obtaining help, reloading the index, and exiting the session.

Use the built-in help command to discover the exact command syntax supported by your current version.

## Design Principles

TextIndex is built around a few simple principles:

1. Solve a real problem first. Every feature should address a concrete need in the personal workflow.
2. Prefer simple data structures. An inverted index is sufficient for the initial keyword-search requirements.
3. Keep the implementation understandable. Small modules and type annotations help make responsibilities and interfaces explicit.
4. Avoid premature optimization. Performance improvements should follow measured bottlenecks, not hypothetical ones.
5. Treat requirements as contracts. Expected behavior should be documented and tested, including edge cases.
6. Remain local and lightweight. Personal notes should be searchable without requiring a remote service or an external search platform.

## Current Limitations

TextIndex is a personal project, and its current implementation is intentionally lightweight.

- The index is stored in memory and is not persisted between sessions.
- Search is based on terms rather than semantic meaning.
- Search results are not yet ranked using a dedicated relevance algorithm such as TF-IDF or BM25.
- Query grammar and operator precedence have limitations that must be considered when composing complex expressions.
- File decoding, unreadable files, and unusual filesystem layouts may require additional validation.
- Search behavior and edge cases still need a dedicated automated test suite.

These limitations define opportunities for future development rather than a commitment to implement every possible feature.

## Roadmap

- [ ] Complete tests for the documented functional contracts.
- [ ] Validate Boolean query semantics and malformed expressions.
- [ ] Improve filesystem error handling and exclusion rules.
- [ ] Refine snippets and search-result presentation.
- [ ] Add relevance ranking if real usage demonstrates the need.
- [ ] Explore incremental indexing and persistent index storage.
- [ ] Improve command-line arguments and local installation.

## Project Structure

The implementation is divided into modules responsible for different parts of the application:

- "main.py" — application entry point and interactive interface.
- "mini_search_engine.py" — search-engine state and coordination.
- "files.py" — file discovery, reading, and index construction.
- "query.py" — query processing and Boolean operations.

The exact boundaries may evolve as the implementation is refactored.

## License

TextIndex is distributed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the conditions of the license.

See the ""LICENSE"" (LICENSE) file for the full license text.

---

TextIndex — because remembering the information is hard enough; remembering which file contains it shouldn't be.
