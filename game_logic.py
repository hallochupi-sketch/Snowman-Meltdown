# game_logic.py

import random
from ascii_art import STAGES

WORDS = ["git", "python", "snow", "winter", "coding"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    return random.choice(WORDS)


def display_game_state(word, guessed_letters, mistakes):
    print(STAGES[mistakes])
    display = " ".join(
        [letter if letter in guessed_letters else "_" for letter in word]
    )
    print(f"Word: {display}")
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")
    print()


def play_game():
    word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    while True:
        display_game_state(word, guessed_letters, mistakes)

        # check win
        if all(letter in guessed_letters for letter in word):
            print("You saved the snowman! 🎉")
            print(f"The word was: {word}")
            break

        # check lose
        if mistakes >= MAX_MISTAKES:
            print("Game Over! The snowman melted. 😢")
            print(f"The word was: {word}")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!\n")
        else:
            mistakes += 1
            print("Wrong guess!\n")
