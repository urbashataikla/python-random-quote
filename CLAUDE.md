# CLAUDE.md

## Project Overview

An educational Python project with two components:

1. **Random Quote Bot** — displays a random quote from a text file (`python get-quote.py`)
2. **English Learning App** — interactive CLI app with vocabulary, conversations, and quizzes (`python run_english_app.py`)

## Repository Structure

```
python-random-quote/
├── CLAUDE.md                        # Guidance for AI assistants
├── README.md                        # Project description
├── get-quote.py                     # Random quote script (skeleton)
├── quotes.txt                       # Quote data (14 quotes)
├── run_english_app.py               # English app entry point
└── english_learning/                # English learning package
    ├── __init__.py
    ├── app.py                       # Main menu and UI logic
    ├── vocabulary.py                # 100 words in 10 categories
    ├── conversations.py             # 10 dialogue scenarios
    └── quiz.py                      # Multiple-choice & fill-in-the-blank
```

## Running

```bash
python run_english_app.py    # Launch English learning app
python get-quote.py          # Random quote (skeleton — needs completion)
```

## Key Details

- **Language:** Python 3, standard library only (no external dependencies)
- **English app features:** vocabulary browser, flashcards, word search, conversation practice, quizzes (multiple choice & fill-in-the-blank), word of the day, statistics
- **Vocabulary:** 100 words across 10 categories (Greetings, Food, Travel, Work, Health, Emotions, Nature, Technology, Education, Daily Life)
- **Conversations:** 10 real-world scenarios (restaurant, airport, job interview, doctor, shopping, directions, hotel, making friends, phone appointment, bank)

## Development Notes

- No external dependencies — uses only `random`, `os`, `sys`, `time`
- No test suite, linter config, or CI/CD pipeline
- Uses 2-space indentation in Python files
- Default branch: `master`

## Conventions

- Keep it simple — educational project, no over-engineering
- Standard library only, no pip packages
- Data lives in Python dicts/lists (vocabulary.py, conversations.py), not external files
- Interactive CLI pattern: clear screen, show menu, get input, loop
