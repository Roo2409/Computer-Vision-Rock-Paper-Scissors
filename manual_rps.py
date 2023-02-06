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
  elif computer_choice == "Rock" and user_choice == "Scissors":
    print("You lost")
    return "computer_choice is a winner"
  else:
    print("You won!")
    return "user_choice is a winner"
   


t1 = get_computer_choice()
print(t1)
t2 = get_user_choice()
print(t2)
t3 = get_winner(t1,t2)
print(t3)
