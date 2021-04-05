#GITHUB TEST Delete me
"""Create a function that generates a random number between
1 and x. User guesses the number and stops when they guess the right one. """
import random
def guess(x):
    random_num = random.randint(1,x)
    #Reset guess value from last time
    guess_value = 0
    print(random_num)
    #Leave loop once random number is guessed value
    while guess_value != random_num:
        #input will default to string so set to int
        guess_value = int(input(f"Enter your guess as an integer between 1 and {x}: "))
        if guess_value < random_num:
            print("Bit too low, try a higher number.")
        #If more than one if or an extra else then use elif
        if guess_value > random_num:
            print("Bit too high, try a lower number.")
    print("Congrats! You are correct.")

"""Create a function that makes the computer guess what number you are thinking
of"""

def computer_guess(high):
    #Set low and high, we tell the computer if it's too high or too low
    low = 0
    #We are giving the computer feedback in terms of high/low
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low, high)
        print(f"My guess is {guess}")
        # The computer will stop when we tell it that it is correct
        feedback = input("Is the number too high (h), too low (l), or Correct (c)? ").lower()
        # Adjust upper and lower bound guess depending on feedback
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        # When low = high then the guess is either low or high
        if low == high:
            guess = low
            break
    print(f"The computer figured it out! The number was {guess}")

computer_guess(10)




