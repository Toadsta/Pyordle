word = "tester"
split_word = list(word)

print(split_word)

guess_word = input("Input a guess word")
split_guess = list(guess_word)

pos = 0
for letter in split_guess:
    if split_guess[pos] == split_word[pos]:
        print(f"The letter {letter} is in the correct place ")
    elif letter in split_word:
        print(f"The letter {letter} is in the word but not the correct place")
    else:
        print(f"The letter {letter} is not in the word")
    pos += 1


