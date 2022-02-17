import random
from word_getter import data
from word_size_getter import list_by_size


def game(size, data):
    word_list = list_by_size(data, int(size))

    chosen_word = random.choice(word_list)

    guesses_remaining = size

    split_word = list(chosen_word)

    print(chosen_word)
    won = False
    while guesses_remaining > 0 and won == False:
        guess = input(f"Enter a {size} letter word: ").lower()
        split_guess = list(guess)
        pos = 0
        for letter in split_guess:
            if split_guess == split_word:
                won = True
            elif split_guess[pos] == split_word[pos]:
                print(f"The letter {letter} is in the correct place ")
            elif letter in split_word:
                print(f"The letter {letter} is in the word but not the correct place")
            else:
                print(f"The letter {letter} is not in the word")
            pos += 1

        if won:
            break
        else:
            guesses_remaining -= 1
            print(f"You have {guesses_remaining} guesses remaining")

    if guesses_remaining > 0:
        print("You Won :)")
    else:
        print("You Lost :(")


game(6, data)
