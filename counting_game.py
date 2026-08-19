"""Counting Game - a small CLI game to practice skip-counting.

Each round the program picks a random starting number and step, shows the first
few terms of the sequence, and asks you to continue it. You score a point for
every correct next term.
"""

import random


def make_sequence(start, step, length):
    """Return `length` terms of an arithmetic sequence."""
    return [start + step * i for i in range(length)]


def play_round(round_number):
    """Play a single round. Return True if the player answers correctly."""
    start = random.randint(1, 20)
    step = random.randint(2, 9)
    shown = make_sequence(start, step, 4)
    answer = start + step * 4

    print(f"\nRound {round_number}: {', '.join(map(str, shown))}, ...")
    try:
        guess = int(input("What is the next number? "))
    except ValueError:
        print("Please enter a whole number - skipping this round.")
        return False

    if guess == answer:
        print("Correct!")
        return True
    print(f"Not quite - the answer was {answer}.")
    return False


def main(rounds=5):
    print("Welcome to the Counting Game!")
    print("Continue each skip-counting sequence.")
    score = sum(play_round(r) for r in range(1, rounds + 1))
    print(f"\nGame over - you scored {score}/{rounds}.")


if __name__ == "__main__":
    main()
