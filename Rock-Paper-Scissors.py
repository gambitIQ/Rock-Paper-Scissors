#CS110A Assignment: Rock-Paper-Scissors Program by Zamambo Mkhize 

import random  

#create a list of choices for the computer to select from at random 
computer_choice = ['rock', 'paper', 'scissors'] 
computer_move = random.choice(computer_choice)  

#start the game
print("Welcome to the Rock-paper-scissors Game! Best out 3 wins!")
 
def game_play():
    
    #game play begins with user input 
    your_move = input("\nPlease enter your move: paper, rock, or scissors: ")

    #create the game conditions for win/lose scenarios
    if computer_move == 'paper':
        print("Computer's move is Paper")
        
        if your_move == 'paper':
            print("Tie with Paper!")
        elif your_move == 'rock':
            print("Computer Wins!", end=" ") 
            print("Paper wins by covering rock!")
        elif your_move == 'scissors' or your_move == 'scissor':
            print("You Win!", end=" ")
            print("Scissors wins by cutting paper")
        else:
            print("Your entry was invalid")
            
    elif computer_move == 'rock':
        print("Computer's move is Rock")
        
        if your_move == 'rock': 
            print("Tie with Rock!")
        elif your_move == 'scissors' or your_move == 'scissor':
            print("Computer Wins!", end =" ")
            print("Rock Breaks Scissors")
        elif your_move == 'paper':
            print("You Win!", end=" ")
            print("Paper wins by covering rock!")
        else:
            print("Your entry was invalid")  
    elif computer_move == 'scissors':
        print("Computer's move is Scissors")
        
        if your_move == 'scissors' or your_move == 'scissor':
            print("Tie with Scissors!")
        if your_move == 'rock':   
            print("You Win!", end =" ")
            print("Rock Breaks Scissors!!")
        elif your_move == 'paper':
            print("Computer Wins!", end=" ")
            print("Scissors win by cutting paper")
        else:
            print("Your entry was invalid")

for i in range(3):
    game_play()
    
    
''' Sample Outputs

Welcome to the Rock-paper-scissors Game! Best out 3 wins!

Please enter your move: paper, rock, or scissors: paper
Computer's move is Rock
You Win! Paper wins by covering rock!

Please enter your move: paper, rock, or scissors: scissor
Computer's move is Rock
Computer Wins! Rock Breaks Scissors

Please enter your move: paper, rock, or scissors: rock
Computer's move is Rock
Tie with Rock!'''