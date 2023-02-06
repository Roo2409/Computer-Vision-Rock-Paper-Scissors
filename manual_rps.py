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
  else:
    print("You won!")
   


b1 = get_computer_choice()
print(b1)
b2 = get_user_choice()
print(b2)
t3 = get_winner(b1,b1)
print(t3)
