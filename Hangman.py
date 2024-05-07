import random
from word_list import words

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word = random.choice(words)
print("The word is " + word)

blanks = ["_" for _ in range(len(word))]
print(blanks)

end_game = False
print("Let's play Hangman. You have 6 lives.")
lives = 6
last_stage_printed = False

while not end_game and lives > 0:
    user_guess = input("Guess a letter: ").lower()

    correct_guess = False
    for i in range(len(word)):
        if user_guess == word[i]:
            blanks[i] = user_guess
            correct_guess = True

    if correct_guess:
        if not last_stage_printed:
            print(stages[-1])
            last_stage_printed = True
    else:
        lives -= 1
        print("Incorrect guess. You have " + str(lives) + " lives left.")
        print(stages[lives])

    print(blanks)

    if "_" not in blanks:
        end_game = True
        print("You win!")

if not end_game:
    print("You lose. The word was " + word)
