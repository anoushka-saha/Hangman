#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

word = word_list[random.randint(0,2)]
print("The word is " + word)

blanks = []
for j in range(len(word)):
    blanks = blanks + ["_"]

print(blanks)

while "_" in blanks:
    user_guess = input(print("Guess a letter: "))

    for i in range(len(word)):
        if user_guess == word[i]:
            blanks[i] = user_guess
    
    print(blanks)

print("You win!")

