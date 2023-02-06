import random
def get_computer_choice():
   list1 = ["Rock","Paper","Scissors"]
   return random.choice(list1)
      
def get_user_choice(): 
  pick_one = input("choose one from list")  
  return pick_one

def get_winner(get_computer_choice , get_user_choice):
  if t1 == t2:
    print("It is a tie!")
  elif t1 == "Rock" and t2 == "Scissors":
    print("You lost")
  else:
    print("You won!")
   


t1 = get_computer_choice()
print(t1)
t2 = get_user_choice()
print(t2)
t3 = get_winner("hi","hello")
print(t3)
