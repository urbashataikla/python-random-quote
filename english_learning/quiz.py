"""Quiz module for testing vocabulary knowledge."""

import random

from english_learning.vocabulary import get_all_words, get_words_by_category, get_categories


def run_vocabulary_quiz(words, num_questions=10):
  """Run a multiple-choice vocabulary quiz and return the score."""
  all_words = get_all_words()
  if len(words) < 4:
    print("Not enough words for a quiz. Need at least 4.")
    return 0, 0

  num_questions = min(num_questions, len(words))
  quiz_words = random.sample(words, num_questions)
  score = 0

  print(f"\n{'=' * 50}")
  print(f"  VOCABULARY QUIZ — {num_questions} Questions")
  print(f"{'=' * 50}")
  print("Choose the correct definition for each word.\n")

  for i, word_entry in enumerate(quiz_words, 1):
    correct_def = word_entry["definition"]

    # Pick 3 wrong answers from other words
    other_words = [w for w in all_words if w["word"] != word_entry["word"]]
    wrong_choices = random.sample(other_words, 3)
    wrong_defs = [w["definition"] for w in wrong_choices]

    # Combine and shuffle options
    options = [correct_def] + wrong_defs
    random.shuffle(options)
    correct_index = options.index(correct_def)

    print(f"Question {i}/{num_questions}: What does \"{word_entry['word']}\" mean?")
    for j, option in enumerate(options):
      print(f"  {j + 1}. {option}")

    while True:
      answer = input("\nYour answer (1-4): ").strip()
      if answer in ("1", "2", "3", "4"):
        break
      print("Please enter 1, 2, 3, or 4.")

    if int(answer) - 1 == correct_index:
      print("Correct!\n")
      score += 1
    else:
      print(f"Wrong. The answer is: {correct_def}\n")

  print(f"{'=' * 50}")
  print(f"  RESULTS: {score}/{num_questions} ({score * 100 // num_questions}%)")
  print(f"{'=' * 50}")

  if score == num_questions:
    print("  Perfect score! Excellent work!")
  elif score >= num_questions * 0.8:
    print("  Great job! You know these words well!")
  elif score >= num_questions * 0.6:
    print("  Good effort! Keep practicing!")
  elif score >= num_questions * 0.4:
    print("  Not bad, but you should review more.")
  else:
    print("  Keep studying! You'll improve with practice.")

  return score, num_questions


def run_fill_in_the_blank(words, num_questions=5):
  """Run a fill-in-the-blank quiz using example sentences."""
  if len(words) < 1:
    print("No words available for this quiz.")
    return 0, 0

  num_questions = min(num_questions, len(words))
  quiz_words = random.sample(words, num_questions)
  score = 0

  print(f"\n{'=' * 50}")
  print(f"  FILL IN THE BLANK — {num_questions} Questions")
  print(f"{'=' * 50}")
  print("Type the missing word to complete each sentence.\n")

  for i, word_entry in enumerate(quiz_words, 1):
    word = word_entry["word"]
    example = word_entry["example"]

    # Replace the word in the example with blanks
    blank_sentence = example.replace(word, "_____")
    # Also try with capitalized version
    blank_sentence = blank_sentence.replace(word.capitalize(), "_____")
    # Handle cases like "I'm" where the word is part of a contraction
    if blank_sentence == example:
      blank_sentence = example.replace(word.lower(), "_____")

    print(f"Question {i}/{num_questions}:")
    print(f"  Definition: {word_entry['definition']}")
    print(f"  Sentence: {blank_sentence}")

    answer = input("\nYour answer: ").strip().lower()

    if answer == word.lower():
      print("Correct!\n")
      score += 1
    else:
      print(f"The answer was: {word}\n")

  print(f"{'=' * 50}")
  print(f"  RESULTS: {score}/{num_questions} ({score * 100 // num_questions}%)")
  print(f"{'=' * 50}")
  return score, num_questions


def run_category_quiz():
  """Let user pick a category and quiz them on it."""
  categories = get_categories()

  print(f"\n{'=' * 50}")
  print("  CATEGORY QUIZ")
  print(f"{'=' * 50}")
  print("\nChoose a category:")
  for i, cat in enumerate(categories, 1):
    print(f"  {i}. {cat}")
  print(f"  {len(categories) + 1}. All categories")

  while True:
    choice = input(f"\nYour choice (1-{len(categories) + 1}): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(categories) + 1:
      break
    print(f"Please enter a number between 1 and {len(categories) + 1}.")

  choice = int(choice)
  if choice == len(categories) + 1:
    words = get_all_words()
    category_name = "All Categories"
  else:
    category_name = categories[choice - 1]
    words = get_words_by_category(category_name)

  print(f"\nQuiz: {category_name} ({len(words)} words)")

  while True:
    num = input(f"How many questions? (1-{len(words)}): ").strip()
    if num.isdigit() and 1 <= int(num) <= len(words):
      break
    print(f"Please enter a number between 1 and {len(words)}.")

  return run_vocabulary_quiz(words, int(num))
