# CLAUDE.md

## Project Overview

A minimal educational Python project that displays random quotes from a text file. Originally designed as a GitHub Learning Lab exercise for Python beginners.

**Run:** `python get-quote.py`

## Repository Structure

```
python-random-quote/
├── CLAUDE.md          # This file — guidance for AI assistants
├── README.md          # Project description and tutorial link
├── get-quote.py       # Main script — entry point
└── quotes.txt         # One quote per line (14 quotes)
```

## Key Details

- **Language:** Python 3 (standard library only, no external dependencies)
- **Entry point:** `get-quote.py` — defines `main()`, guarded by `if __name__ == "__main__"`
- **Data file:** `quotes.txt` — plain text, one quote per line
- **Current state:** The main script has core logic commented out (skeleton for learners to complete). The intended implementation reads `quotes.txt`, selects a random line, and prints it.

## Development Notes

- No dependency files (no requirements.txt, setup.py, or pyproject.toml)
- No test suite, linter config, or CI/CD pipeline
- No .gitignore
- Uses 2-space indentation in Python files
- Default branch: `master`

## Conventions

- Keep it simple — this is a single-script educational project
- Quotes are stored as plain text lines in `quotes.txt`
- No external packages; use only the Python standard library (`random`, `open()`)
