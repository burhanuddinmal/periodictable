import random
from words import words
import string

#importing words.py in this file to get all the words
def get_valid_word(words):
    word = random.choice(words) #randomly choses a word from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #keeping track of the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keeping track of letters which the user has guessed
    lives = 6
    #getting users input
    while len(word_letters) > 0 and lives > 0:
        # to show the letters used
        #' '.join(['a', 'b', 'cd']) --> 'a b cd'
          print("You have", lives,"lives left and you have used the letters: ", ' '.join(used_letters))
        #what the current word is (w_rd)
          word_list = [letter if letter in used_letters else '-' for letter in word]
          print("Current word: ", ' '.join(word_list))
          user_letter = input("GUESS A LETTER : ").upper()
          if user_letter in alphabet - used_letters:
              used_letters.add(user_letter)
              if user_letter in word_letters:
                  word_letters.remove(user_letter)
              else:
                  lives = lives - 1 #takes away a life away
                  print("Letter is not in the word.")
          elif user_letter in used_letters:
              print("You've already used that character .Please try again.")

    else:
        print("You have typed an invalid character.Please try again")
    if lives == 0:
        print("You have died the word was ", word)
    else:
        print("you guessed the word ", word ,"!!")

hangman()
user_input = input("TYPE A LETTER:")
print(user_input)
