# DevKB-CLI - Command Line Interface for Developer Knowledge Base

A lightweight CLI tool for managing code snippets and documentation from your terminal.

## Features

- Add, search, and manage code snippets from CLI
- Semantic search powered by local embeddings
- Support for multiple programming languages
- Fast and efficient - no web server needed
- SQLite storage for offline use

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Add a snippet
```bash
python -m cli add --file path/to/code.py --title "My Snippet"
```

### Search
```bash
python -m cli search "how to sort a list"
```

### List all snippets
```bash
python -m cli list
```

### Delete a snippet
```bash
python -m cli delete 1
```

## Configuration

Copy `.env.example` to `.env` and configure:
```
DATABASE_PATH=./data/snippets.db
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

## License

MIT
