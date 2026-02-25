"""
Snowman Meltdown — a Hangman-style word guessing game.
Guess the word before the snowman melts away completely!
"""

import random

# ── Snowman ASCII art stages (0 = intact, 6 = melted) ──────────────────────
SNOWMAN_STAGES = [
    # Stage 0 — Fully built
    """
       _===_
      (o   o)
      ( > < )
     /|  ^  |\\
    / |_____|  \\
      |     |
     _|_____|_
    """,
    # Stage 1 — Hat gone
    """
    
      (o   o)
      ( > < )
     /|  ^  |\\
    / |_____|  \\
      |     |
     _|_____|_
    """,
    # Stage 2 — Head drooping
    """
    
      (. . .)
      (  _  )
     /|     |\\
    / |_____|  \\
      |     |
     _|_____|_
    """,
    # Stage 3 — Arms gone
    """
    
      (. . .)
      (  _  )
       |     |
       |_____|
       |     |
      _|_____|_
    """,
    # Stage 4 — Body shrinking
    """
    
      (x   x)
      (_____)
       |     |
       |_____|
    """,
    # Stage 5 — Almost melted
    """
    
       (~_~)
       /___\\
    """,
    # Stage 6 — Melted puddle
    """
    
      ~~~~~~~
    *  R.I.P  *
      ~~~~~~~
    """,
]

MAX_WRONG = len(SNOWMAN_STAGES) - 1  # 6 wrong guesses allowed

# ── Word list ───────────────────────────────────────────────────────────────
WORDS = [
    # Nature / winter
    "blizzard", "avalanche", "glacier", "snowflake", "frostbite", "icicle",
    "hibernation", "solstice", "tundra", "permafrost",
    # Animals
    "penguin", "walrus", "polar bear", "reindeer", "arctic fox",
    # General
    "fireplace", "mittens", "chimney", "toboggan", "snowboard",
    "cocoa", "scarf", "lantern", "evergreen", "sleigh",
    # Tech / pop culture
    "python", "keyboard", "algorithm", "database", "encryption",
    "satellite", "hologram", "quantum", "robot", "cyborg",
]

# Filter out multi-word entries for simpler play (optional)
WORDS = [w for w in WORDS if " " not in w]


def choose_word() -> str:
    return random.choice(WORDS).lower()


def display_state(word: str, guessed: set, wrong: int) -> None:
    print(SNOWMAN_STAGES[wrong])
    print(f"  Wrong guesses: {wrong}/{MAX_WRONG}")
    print()

    # Show word with blanks
    display = " ".join(c if c in guessed else "_" for c in word)
    print(f"  Word: {display}")
    print()

    if guessed - set(word):  # show only actually wrong letters
        wrong_letters = sorted(guessed - set(word))
        print(f"  Wrong letters: {', '.join(wrong_letters)}")
    print()


def get_guess(guessed: set) -> str:
    while True:
        raw = input("  Guess a letter: ").strip().lower()
        if len(raw) != 1 or not raw.isalpha():
            print("  ⚠  Please enter a single letter.")
        elif raw in guessed:
            print(f"  ⚠  You already guessed '{raw}'. Try another.")
        else:
            return raw


def play() -> None:
    print("\n" + "=" * 40)
    print("   ❄  SNOWMAN MELTDOWN  ❄")
    print("   Guess the word before he melts!")
    print("=" * 40)

    word = choose_word()
    guessed: set = set()
    wrong = 0

    while wrong < MAX_WRONG:
        display_state(word, guessed, wrong)

        if all(c in guessed for c in word):
            print(f"  🎉  You saved the snowman! The word was: {word.upper()}")
            break

        letter = get_guess(guessed)
        guessed.add(letter)

        if letter in word:
            print(f"  ✅  Nice! '{letter}' is in the word.\n")
        else:
            wrong += 1
            print(f"  ❌  Nope! The snowman is melting… ({MAX_WRONG - wrong} chances left)\n")
    else:
        display_state(word, guessed, wrong)
        print(f"  💧  The snowman melted! The word was: {word.upper()}")

    print()


def main() -> None:
    while True:
        play()
        again = input("  Play again? (y/n): ").strip().lower()
        if again != "y":
            print("\n  Stay frosty. 👋\n")
            break


if __name__ == "__main__":
    main()
