import random
from word_getter import data
from word_size_getter import list_by_size

size = 5  # input("How long of a word would you like to guess?")

word_list = list_by_size(data, int(size))

chosen_word = random.choice(word_list)

guesses_remaining = size

split_word = list(chosen_word)

print(chosen_word)
won = False
while guesses_remaining > 0 and won == False:
    guess = input(f"Enter a {size} letter word: ")
    split_guess = list(guess)
    pos = 0
    for letter in split_guess:
        if split_guess[pos] == split_word[pos]:
            print(f"The letter {letter} is in the correct place ")
            won = True
            break
        elif letter in split_word:
            print(f"The letter {letter} is in the word but not the correct place")
        else:
            print(f"The letter {letter} is not in the word")
        pos += 1
    guesses_remaining -= 1
    print(guesses_remaining)

if guesses_remaining > 0:
    print("You Won :)")
else:
    print("You Lost :(")
