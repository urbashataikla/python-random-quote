"""Main English Learning App — interactive CLI menu."""

import os
import random
import sys
import time

from english_learning.vocabulary import (
  VOCABULARY, get_all_words, get_categories, get_words_by_category,
)
from english_learning.conversations import (
  get_all_conversations, get_conversation_titles, get_conversation_by_index,
)
from english_learning.quiz import (
  run_vocabulary_quiz, run_fill_in_the_blank, run_category_quiz,
)


def clear_screen():
  os.system("cls" if os.name == "nt" else "clear")


def press_enter():
  input("\nPress Enter to continue...")


def print_banner():
  print("=" * 56)
  print("     ENGLISH LEARNING APP")
  print("     Vocabulary | Conversations | Quizzes")
  print("=" * 56)


# ── Vocabulary Browser ──────────────────────────────────


def browse_vocabulary():
  """Browse vocabulary by category."""
  categories = get_categories()

  while True:
    clear_screen()
    print(f"\n{'=' * 50}")
    print("  VOCABULARY — Choose a Category")
    print(f"{'=' * 50}\n")

    for i, cat in enumerate(categories, 1):
      count = len(get_words_by_category(cat))
      print(f"  {i}. {cat} ({count} words)")
    print(f"\n  0. Back to main menu")

    choice = input(f"\nYour choice (0-{len(categories)}): ").strip()
    if choice == "0":
      return
    if not choice.isdigit() or not (1 <= int(choice) <= len(categories)):
      continue

    show_category_words(categories[int(choice) - 1])


def show_category_words(category):
  """Display all words in a category."""
  words = get_words_by_category(category)

  clear_screen()
  print(f"\n{'=' * 50}")
  print(f"  {category.upper()}")
  print(f"{'=' * 50}\n")

  for i, w in enumerate(words, 1):
    print(f"  {i}. {w['word']}")
    print(f"     Definition: {w['definition']}")
    print(f"     Example:    \"{w['example']}\"")
    print()

  press_enter()


# ── Flashcard Mode ───────────────────────────────────────


def flashcard_mode():
  """Study vocabulary with flashcards."""
  all_words = get_all_words()

  clear_screen()
  print(f"\n{'=' * 50}")
  print("  FLASHCARD MODE")
  print(f"{'=' * 50}")
  print("\nYou'll see a word. Try to recall its meaning,")
  print("then press Enter to reveal the definition.")
  print("Type 'q' to quit.\n")

  random.shuffle(all_words)
  studied = 0

  for word_entry in all_words:
    print(f"  Word: {word_entry['word'].upper()}")
    print(f"  Category: {word_entry['category']}")
    response = input("\n  (Press Enter to reveal, 'q' to quit) ")

    if response.strip().lower() == "q":
      break

    print(f"\n  Definition: {word_entry['definition']}")
    print(f"  Example:    \"{word_entry['example']}\"")
    studied += 1

    response = input("\n  (Press Enter for next, 'q' to quit) ")
    if response.strip().lower() == "q":
      break
    print()

  print(f"\n  You studied {studied} word(s). Great job!")
  press_enter()


# ── Word Search ──────────────────────────────────────────


def search_word():
  """Search for a word in the vocabulary."""
  clear_screen()
  print(f"\n{'=' * 50}")
  print("  WORD SEARCH")
  print(f"{'=' * 50}")

  query = input("\nEnter a word to search: ").strip().lower()
  if not query:
    return

  all_words = get_all_words()
  results = [w for w in all_words if query in w["word"].lower()]

  if results:
    print(f"\nFound {len(results)} result(s):\n")
    for w in results:
      print(f"  {w['word']} [{w['category']}]")
      print(f"    Definition: {w['definition']}")
      print(f"    Example:    \"{w['example']}\"")
      print()
  else:
    print(f"\nNo results found for \"{query}\".")
    # Suggest close matches
    suggestions = [w for w in all_words if query[:3] in w["word"].lower()]
    if suggestions:
      print("Did you mean:")
      for w in suggestions[:5]:
        print(f"  - {w['word']}")

  press_enter()


# ── Conversation Practice ───────────────────────────────


def conversation_menu():
  """Choose and practice a conversation scenario."""
  while True:
    clear_screen()
    titles = get_conversation_titles()

    print(f"\n{'=' * 50}")
    print("  CONVERSATION PRACTICE")
    print(f"{'=' * 50}\n")

    for i, title in enumerate(titles, 1):
      print(f"  {i}. {title}")
    print(f"\n  0. Back to main menu")

    choice = input(f"\nYour choice (0-{len(titles)}): ").strip()
    if choice == "0":
      return
    if not choice.isdigit() or not (1 <= int(choice) <= len(titles)):
      continue

    show_conversation(int(choice) - 1)


def show_conversation(index):
  """Display a conversation with interactive reading."""
  conv = get_conversation_by_index(index)
  if not conv:
    return

  clear_screen()
  print(f"\n{'=' * 50}")
  print(f"  {conv['title'].upper()}")
  print(f"{'=' * 50}")
  print(f"\n  {conv['description']}\n")
  print("  (Press Enter to advance the dialogue)\n")

  for speaker, line in conv["dialogue"]:
    if speaker == "You":
      print(f"  >> You: {line}")
    else:
      print(f"     {speaker}: {line}")
    input()

  print(f"\n{'-' * 50}")
  print("  KEY PHRASES TO REMEMBER:")
  print(f"{'-' * 50}")
  for phrase in conv["key_phrases"]:
    print(f"    - {phrase}")

  press_enter()


# ── Quiz Menu ────────────────────────────────────────────


def quiz_menu():
  """Choose a quiz type."""
  while True:
    clear_screen()
    print(f"\n{'=' * 50}")
    print("  QUIZ CENTER")
    print(f"{'=' * 50}\n")
    print("  1. Multiple Choice Quiz (by category)")
    print("  2. Multiple Choice Quiz (all words)")
    print("  3. Fill in the Blank")
    print("\n  0. Back to main menu")

    choice = input("\nYour choice (0-3): ").strip()

    if choice == "0":
      return
    elif choice == "1":
      clear_screen()
      run_category_quiz()
      press_enter()
    elif choice == "2":
      clear_screen()
      all_words = get_all_words()
      while True:
        num = input(f"\nHow many questions? (1-{len(all_words)}): ").strip()
        if num.isdigit() and 1 <= int(num) <= len(all_words):
          break
        print(f"Please enter a number between 1 and {len(all_words)}.")
      run_vocabulary_quiz(all_words, int(num))
      press_enter()
    elif choice == "3":
      clear_screen()
      all_words = get_all_words()
      while True:
        num = input(f"\nHow many questions? (1-{len(all_words)}): ").strip()
        if num.isdigit() and 1 <= int(num) <= len(all_words):
          break
        print(f"Please enter a number between 1 and {len(all_words)}.")
      run_fill_in_the_blank(all_words, int(num))
      press_enter()


# ── Daily Word ───────────────────────────────────────────


def daily_word():
  """Show a random word of the day."""
  all_words = get_all_words()
  word = random.choice(all_words)

  clear_screen()
  print(f"\n{'=' * 50}")
  print("  WORD OF THE DAY")
  print(f"{'=' * 50}\n")
  print(f"  {word['word'].upper()}")
  print(f"  Category: {word['category']}")
  print(f"\n  Definition: {word['definition']}")
  print(f"  Example:    \"{word['example']}\"")
  print(f"\n{'=' * 50}")

  press_enter()


# ── Stats ────────────────────────────────────────────────


def show_stats():
  """Show vocabulary statistics."""
  categories = get_categories()
  total = len(get_all_words())

  clear_screen()
  print(f"\n{'=' * 50}")
  print("  VOCABULARY STATISTICS")
  print(f"{'=' * 50}\n")
  print(f"  Total words: {total}")
  print(f"  Categories:  {len(categories)}\n")

  for cat in categories:
    count = len(get_words_by_category(cat))
    bar = "#" * count
    print(f"  {cat:<25s} {count:>3d}  {bar}")

  print(f"\n  Conversations available: {len(get_all_conversations())}")

  press_enter()


# ── Main Menu ────────────────────────────────────────────


def main():
  """Main application loop."""
  while True:
    clear_screen()
    print_banner()
    print()
    print("  1. Browse Vocabulary")
    print("  2. Flashcard Study")
    print("  3. Search a Word")
    print("  4. Conversation Practice")
    print("  5. Take a Quiz")
    print("  6. Word of the Day")
    print("  7. Statistics")
    print()
    print("  0. Exit")

    choice = input("\nYour choice (0-7): ").strip()

    if choice == "0":
      clear_screen()
      print("\nGoodbye! Keep learning English every day!\n")
      sys.exit(0)
    elif choice == "1":
      browse_vocabulary()
    elif choice == "2":
      flashcard_mode()
    elif choice == "3":
      search_word()
    elif choice == "4":
      conversation_menu()
    elif choice == "5":
      quiz_menu()
    elif choice == "6":
      daily_word()
    elif choice == "7":
      show_stats()


if __name__ == "__main__":
  main()
