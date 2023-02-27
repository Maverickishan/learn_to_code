import random

def get_choice():
    player_choice=input("enter  any of rock, paper, scissor:")
    option=["rock","paper","scissor"]
    computer_choice = random.choice(option)
    choices = {"player": player_choice , "computer": computer_choice}
    return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer} ")
    if player==computer:
      return "its a tie"
    elif player== "rock":
      if computer == " scissor":
       return " you win, rock crushes the scissor"
      else:
       return"paper cover rock, you lose!"
    elif player== "paper":
      if computer ==" rock":
        return " you win,paper cover rock "
      else:
        return " you lose , scissor cut paper"
    elif player== "scissor":
      if computer =="paper":
        return " you win,scissor cut paper "
      else:
        return " you lose , rock smashes scissor"
      

choices = get_choice( )
result = check_win(choices["player"], choices["computer"]) 
print(result)


