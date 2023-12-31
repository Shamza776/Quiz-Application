###SIMPLE ROCK PAPER SCISSORS GAME BETWEEN PLAYER AND COMPUTER
import random
listOfElements = ['Rock', 'Paper', 'Scissors']
computerChoice= random.choice(listOfElements)
playerChoice = input('pick a choice: ').lower
#playerChoice = 'Rock'
while True:
     
    def newGame ():
        if playerChoice == computerChoice:
            print("it's a tie, play again")
        elif (playerChoice == "Rock" and computerChoice == "Scissors") or \
            (playerChoice=="Paper"  and  computerChoice == "Rock")  or \
            (playerChoice== "Scissors" and computerChoice == "Paper"):
            print('you win')
        elif (playerChoice == "Paper" and computerChoice == "Scissors") or \
            (playerChoice=="Scissors"  and  computerChoice == "Rock")  or \
            (playerChoice== "Rock" and computerChoice == "Paper"):
            print('you lose')
        else:
            print ('Invalid Input')
    newGame()
    while playerChoice not in listOfElements:
        playerChoice = input('Enter Rock, Paper, or Scissors: ')
        playerChoice = playerChoice.capitalize()
    play_again = input('play again? (yes or no): ')
    #play_again = 'yes'
    if play_again == 'yes':
        newGame()
    else:
        break
print('Thanks for playing!Bye')




