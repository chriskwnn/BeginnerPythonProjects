import random
#Import list of words from the python file in same directory called WordsList
from WordsList import words
import string

#Function that picks a word that is valid, some words have spaces or hyphens so pick until it is valid
def pickWord():
    SelectedWord = random.choice(words)
    #Note to self: while loop runs until statement is false
    while "-" in SelectedWord or " " in SelectedWord:
        SelectedWord = random.choice(words)
    return SelectedWord.upper()

#Function returns positions of characters
def itemPositions(list,letter):
    positions = []
    for a in range(len(list)):
        if letter == list[a]:
            positions.append(a)
    return positions

#Function that fills empty list with blank spaces in length of word
def emptyList(LettersinWord):
    CorrectLetters = []
    for i in range(len(LettersinWord)):
        CorrectLetters.append(" ")
    return CorrectLetters

#Create function for hangman game
def hangman():
    SelectedWord = pickWord()
    #Create variable that contains all the letters in the selected word
    LettersinWord = list(SelectedWord)
    #Create a variable that contains all the alphabet
    alphabet = list(string.ascii_uppercase)
    #Create variable that contains all letters you've guessed
    GuessedLetters = []
    CorrectLetters = emptyList(LettersinWord)
    MaxAllowableGuessFail = 6

    while MaxAllowableGuessFail > 0:
        letter = str(input("Guess a letter in the word: ")).upper()
        #User has to try again if letter entered not in alphabet or already guessed
        while (letter in GuessedLetters) or (letter not in alphabet):
            letter = str(input("Invalid input. Try again: ")).upper()
        #Put letter in GuessedLetters if not guessed yet
        GuessedLetters.append(letter)
        #Check if letter is in LettersinWord, if it is return positions and add correct letters to positions
        if letter in LettersinWord:
            positions = itemPositions(LettersinWord, letter)
            for i in range(len(positions)):
                letterlocation = positions[i]
                CorrectLetters[letterlocation] = letter
            print(f"You guessed correctly! The letter {letter} is in the word.")
        #If you guess the wrong letter you lose an allowable  guess
        else:
            MaxAllowableGuessFail-= 1
        #If you correctly guess all the letters
        if " " not in CorrectLetters:
            print(f"You Win! The word was {SelectedWord}")
            return
        #Status of game for user so far
        print(f"Here are the letters you've guessed: {GuessedLetters}")
        print(f"Correct letters so far: {CorrectLetters}")
        print(f"You have {MaxAllowableGuessFail} wrong guesses left")
        #Provide spacing in console
        print("\n")
    print(f"Oh no! You lose, the word was: {SelectedWord}")



hangman()