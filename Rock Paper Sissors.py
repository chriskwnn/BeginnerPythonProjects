import random
#Create function that plays the game
def play():
    # User input rock paper or sissors
    player = input("Enter your choice, rock = r, sissors = s, paper = p: ").lower()
    """Q: If user puts in response other than possible rock paper or sissor, not really sure why
    I can't use while player != r or player != s etc. 
    
    A: So apparently the While loop runs until the statement becomes false, so when player == r,s, and p 
    at the same time which is not possible. Therefore, you need to use AND instead.
    so it will return false when either of the statements are true
    
    From StackOverflow: A while loop will continue as long as its condition is true. If you have two conditions connected with an or, 
    the loop will only end once both are false, as if one is true then the entire or is true."""

    while player != "r" and player != "s" and player != "p":
        print("invalid choice")
        player = input("Enter your choice, rock = r, sissors = s, paper = p: ").lower()

    #Computer chooses rock paper or sissors
    ComputerChoice = random.choice(["r","p","s"])
    win = GameRules(player,ComputerChoice)
    if win == "w":
        print(f"Congrats, you win. You picked {player} and the computer picked {ComputerChoice}")
    elif win == "l":
        print(f"You lose. You picked {player} and the computer picked {ComputerChoice}")
    elif win == "t":
        print(f"It's a tie. You picked {player} and the computer picked {ComputerChoice}. Play again.")

#Define rules of the game as a function. So the play game function uses the rule function to check if you win/lose
def GameRules(player,ComputerChoice):
    #r>s, p>r, s>p
    #Define tie game
    if player == ComputerChoice:
        return "t"
    elif (player == "r" and ComputerChoice == "s") or (player == "p" and ComputerChoice == "r") or (player == "s" and ComputerChoice == "p"):
        return "w"
    return "l"

play()