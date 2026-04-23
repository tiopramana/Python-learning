# Hang name fruits guesser

import random

words = ("apple", "orange", "manggo", "banana", "pineapple", "coconut")

hangman_art = {0:("   ",
                "   ",
                "   "),
                1:(" * ",
                "   ",
                "   "),
                2:(" * ",
                " | ",
                "   ",),
                3:(" * ",
                   "/| ",
                   "   "),
                4:(" * ",
                   "/|\\",
                   "   "),
                5:(" * ",
                   "/|\\",
                   "/   "),
                6:(" * ",
                   "/|\\",
                   "/ \\")
                }

def display_name(wrong_gues):
    print("=========")
    for line in hangman_art[wrong_gues]:
        print(line)
    print("=========")


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_gues = 0
    guest_letter = set()
    is_running = True

    while is_running:
        display_name(wrong_gues)
        display_hint(hint)
        print()
        guess = input("Gues the letter : ").lower()

        if len(guess) != 1 :
            print("Please enter gues character!")
            continue
        elif not guess.isalpha():
            print("Please enter character not a number!")
            continue

        if guess in guest_letter:
            print(f"Guess already {guess} guessed")
            continue

        guest_letter.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gues += 1

        if "_" not in hint:
            display_name(wrong_gues)
            display_answer(answer)
            print("You win!!")
            is_running = False
        elif wrong_gues >= len(hangman_art) - 1:
            display_name(wrong_gues)
            display_answer(answer)
            print("You lose!!")
            is_running = False

if __name__ == '__main__':
        main()
