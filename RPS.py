from tkinter import *
import tkinter.font as font
import random 

#initial scores
player_Score=0
computer_Score=0

#Game options for the computer
options=[('rock',0),('paper',1),('scissors',2)]

#function for computer wins 
def computer_wins():
    global computer_Score, player_Score
    computer_Score += 1
    winner_label.config(text="Computer Won!") 
    computer_score_label.config(text="Computer Score: " + str(computer_Score))
    player_score_label.config(text="Player Score: "+ str(player_Score))

#functions for player wins 
def player_wins():
    global computer_Score, player_Score
    player_Score += 1
    winner_label.config(text="Player Won!") 
    computer_score_label.config(text="Computer Score: "+ str(computer_Score))
    player_score_label.config(text="Player Score: " + str(player_Score))

#function for tie 
def tie():
    global computer_Score, player_Score
    winner_label.config(text="TIE!!") 
    computer_score_label.config(text="Computer Score: "+ str(computer_Score))
    player_score_label.config(text="Player Score: " + str(player_Score))
#Main function : player choice function 
def player_choice(player_input):
    global computer_Score, player_Score

    print(player_input) 
    computer_input=get_computer_choice()
    print(computer_input)
    #update the selection on screen.
    player_choice_label.config(text="Your Selection"+ player_input[0])
    computer_choice_label.config(text="Computer Selection"+ computer_input[0])
    
    #If player and computer choose the same option.
    if player_input == computer_input:
        tie()
    
    #player chooses Rock 
    elif player_input[1]==0:
        if computer_input[1] == 1:
            computer_wins()
        elif computer_input[1] ==2:
            player_wins()
    
    #player chooses paper
    elif player_input[1] == 1:
        if computer_input[1] ==0:
            player_wins()
        elif computer_input[1] == 2:
            computer_wins()
    
    #player chooses scissors 
    elif player_input[1] ==2:
        if computer_input[1]==0:
            computer_wins()
        elif computer_input[1] ==1:
            player_wins()
# function to randomly select computer choice    
def get_computer_choice():
    return random.choice(options)

# ------ GUI -- Part  -----
game_window = Tk()
game_window.title("Rock Paper Scissors")

#font settings 
app_font = font.Font(font="Roboto",size=12)

#Game Title 
game_title = Label(text="Rock Paper Scissors ", font=-font.Font(size=20),fg="grey")
game_title.pack()












    

