"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""

import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
    
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
  
    # convert name to number using if/elif/else
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Not a valid choice!")
        
    # don't forget to return the result!
   
    pass
    
def number_to_name(number):
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Not a valid number!")
    
    pass


def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS 
    and print results to console
    """
    
    # print a blank line to separate consecutive games
    print("\n")
    
    # print out the message for the player's choice
    print("Player chooses", player_choice)
    
    # convert the player's choice to player_number using the function name_to_number()
    player_choice_num = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out message for computer's choice
    print("Computer chooses", comp_choice)

    # compute difference of player_number and comp_number modulo five
    result_num = (comp_number - player_choice_num) % 5

    # use if/elif/else to determine winner and print winner message
    if result_num == 1 or result_num == 2:
        print("Computer Wins!")
    elif result_num == 3 or result_num == 4:
        print("Player Wins!")
    else:
        print("It is a Tie!")
    
    pass
     
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

