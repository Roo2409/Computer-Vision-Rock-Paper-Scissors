import random
def get_computer_choice():
   list1 = ["Rock","Paper","Scissors"]
   return random.choice(list1)
      
def get_user_choice(): 
  pick_one = input("choose one from list")  
  return pick_one

def get_winner(computer_choice , user_choice):
  if computer_choice == user_choice:
    print("It is a tie!")
    winner = "tie"
  elif computer_choice == "Rock"and user_choice == "Scissors":
    print("You lost")
    winner = "computer_choice"
  elif computer_choice == "Paper" and user_choice == "Rock":
    print("You lost")
    winner = "computer_choice"
  elif computer_choice == "Scissors"and user_choice == "Paper":
    print("You lost")
    winner = "computer_choice"
  else:
    print("You won!")
    winner = "user_choice"
  return winner
   


t1 = get_computer_choice()
print(t1)
t2 = get_user_choice()
print(t2)
t3 = get_winner(t1,t2)
print(t3)
