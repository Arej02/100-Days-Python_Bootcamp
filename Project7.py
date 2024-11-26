import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
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
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word = [
    "apple", "orange", "banana", "grape", "cherry", "peach",
    "plum", "pear", "mango", "melon", "kiwi", "papaya",
    "pineapple", "blueberry", "strawberry", "raspberry",
    "blackberry", "coconut", "pomegranate", "apricot"
]
chosen_word=random.choice(word)
print(chosen_word)

place_holder=""

for char in chosen_word:
    place_holder+="_"

game_over=False

correct_letters=[]
lives = 6

while not game_over:
    guess = input("Enter a letter:").lower()
    display = ""
    for char in chosen_word:
        if char==guess:
            display+=char
            correct_letters.append(char)
            print(f"You have guessed the letter{guess} correctly!")
        elif char in correct_letters:
            display+=char
        else:
            display+="_"


    print(display)

    if "_" not in display:
        game_over=True
        print("You win!")

    if guess not in chosen_word:
        lives-=1
        print(f"The word {guess} in incorrect.You have {lives} remaining")
        if lives==0:
            game_over=True
            print("You lose!")



    print(stages[lives])