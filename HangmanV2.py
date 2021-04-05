#Following optimized youtube tutorial, see HangmanV1 for my personal version:
import random
from WordsList import words
import string

#Get a valid word
def ValidWord():
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.chocie(words)
    return word.upper()

#Hangman game
def hangman():
    word = ValidWord()
    word_letters = set(word) #The letters in the word as a set. Unordered, unchangeable and no duplicates. You can remove and add values though.
    alphabet = set(string.ascii_uppercase)
    #Set containing what user has guessed
    guessed_letters = set()
    #Tries avaliable or you lose
    FailedGuesses = 6
    #Keep guessing until you guess the word
    while len(word_letters) != 0 and FailedGuesses != 0: #stops when statement is false
        print("The letters you have used so far: ", " ".join(guessed_letters))
        print(f"You have {FailedGuesses} wrong guesses left")
        #Q: How does this work?
        """A: Focus on the for x in word first. This means that you will be looping through the length of 
        of word and grabbing the letter each time you loop through it, denoted as x. 
        
        Now lets look at the first part, x, this indicates that every time you loop through you are inserting
        the letter you grabbed into the current position of the currentOutput list. Alternatively, if you
        replaced x with 0 it would put the character 0 in instead of the letter you grabbed.
        
        Now lets look at the next part, the if/else statement. If we didnt have this, the player will
        be able to see the whole word when they play. So we need to only show letters they have correctly
        guessed and hide unguessed letters with a -
        
        To summarize: Loop through the word, and populating the list with correctly guessed letters
        and hide letters not guessed yet with -"""
        currentOutput = [x if x in guessed_letters else "-" for x in word]
        print("Progress: "," ".join(currentOutput))

        user_input = input("Please enter a letter: ").upper()
        #If valid letter then add to guessed_letters
        if user_input in alphabet - guessed_letters:
            guessed_letters.add(user_input)
            #If you correctly guessed then remove that letter from the selected word list
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                FailedGuesses -= 1
        elif user_input in guessed_letters:
            print("Invalid input, you guessed this letter already.")
        else:
            print("Invalid input, letter entered does not exist.")

    if FailedGuesses == 0:
        print(f"Oh no! You lost, the word was {word}")
    else:
        print(f"Congrats! You win, the word was {word}")

hangman()

