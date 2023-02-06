import random
def get_computer_choice():
   return random.choice(list)
      
def get_user_choice(): 
  pick_one = input("choose one from list")  
  if pick_one in list:
     return pick_one
  else:
     print("wrong letter")


list = ["rock","paper","scissor"]
t1= get_computer_choice()
print(t1)
t2 = get_user_choice()
print(t2)
