# main.py

import os
import random
from ascii_art import STAGES


WORD_LIST = ["git", "python", "snow", "winter", "coding"]


def clear_screen():
    # On Windows, use "cls"; on Linux/macOS, use "clear"
    os.system("cls" if os.name == "nt" else "clear")


def get_valid_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly one character.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (A–Z).")
            continue
        if guess in already_guessed:
            print("You already guessed that letter. Try another one.")
            continue
        return guess


def display_state(wrong_guesses, word, guessed_letters, current_state):
    clear_screen()
    print(STAGES[wrong_guesses])
    print()
    print("Word:", " ".join(current_state))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print(f"Wrong guesses: {wrong_guesses}/{len(STAGES) - 1}")
    print()


def play_game():
    secret_word = random.choice(WORD_LIST)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(STAGES) - 1

    current_state = ["_" for _ in secret_word]

    while True:
        display_state(wrong_guesses, secret_word, guessed_letters, current_state)

        # Check win
        if "_" not in current_state:
            print(f"You win! The word was: {secret_word}")
            break

        # Check lose
        if wrong_guesses >= max_wrong:
            print("Game Over! The snowman has melted!")
            print(f"The word was: {secret_word}")
            break

        guess = get_valid_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            for i, ch in enumerate(secret_word):
                if ch == guess:
                    current_state[i] = guess
        else:
            wrong_guesses += 1


def main():
    while True:
        play_game()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
