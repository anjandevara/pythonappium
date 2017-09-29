class Game:

# Creating a constructor
    def __init__(self, newPlayerName):
        self.playerName = newPlayerName
        self.playerHand = "NA"
        self.botHand = "NA"
        self.winner = "No winner yet"
        print("New instance of game class for :: " + self.playerName)


# Define a behaviour for our game class
    def runGame(self):
        if((self.playerHand == "rock" or self.playerHand == "ROCK") and self.botHand == 1):
            self.winner == "You WIN!!"
        elif ((self.playerHand == "rock" or self.playerHand == "ROCK") and self.botHand == 2):
            self.winner == "You TIE!!"
        elif ((self.playerHand == "rock" or self.playerHand == "ROCK") and self.botHand == 3):
            self.winner == "You LOSE!!"
        elif ((self.playerHand == "paper" or self.playerHand == "PAPER") and self.botHand == 1):
            self.winner == "You LOSE!!"
        elif ((self.playerHand == "paper" or self.playerHand == "PAPER") and self.botHand == 2):
            self.winner == "You WIN!!"
        elif ((self.playerHand == "paper" or self.playerHand == "PAPER") and self.botHand == 3):
            self.winner == "You TIE!!"
        elif ((self.playerHand == "scissors" or self.playerHand == "SCISSORS") and self.botHand == 1):
            self.winner == "You TIE!!"
        elif ((self.playerHand == "scissors" or self.playerHand == "SCISSORS") and self.botHand == 2):
            self.winner == "You LOSE!!"
        elif ((self.playerHand == "scissors" or self.playerHand == "SCISSORS") and self.botHand == 3):
            self.winner == "You WIN!!"
        else:
            self.winner = "Invalid Input. Try again!!"

def main():
    myGame = Game("Anjan")

    print(myGame.playerName)
    print(myGame.playerHand)
    print(myGame.botHand)
    print(myGame.winner)

    print()

    myGame.playerHand = "paper"
    myGame.botHand = "1"
    myGame.runGame()
    print(myGame.winner)

main()