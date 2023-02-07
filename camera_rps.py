import cv2
import numpy as np
import random

def get_prediction():
    return 
cv2.imshow()
def timetime():
    print("you can choose rock")
timetime()
computer_wins = 0
user_wins=0
round = 0
list1 = ["Rock","Paper","Scissors"]
while computer_wins <3 and user_wins <3:
  print ("Starting round ", round + 1)
  print ("-----------------------")
  computer_choice = random.choice(list1)
  user_choice = input("choice rock , paper, scissor")
  
  print (f"computer_choice choose : {computer_choice} and user_choice choose {user_choice}")
  if computer_choice == user_choice:
    print("It's a tie!")
  elif (computer_choice == "Rock"and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors"and user_choice == "Paper"):
    print("computer_choice You win!")
    computer_wins += 1
  else: 
    print("user_choice you win")
    user_wins +=1
round +=1
if computer_wins > user_wins:
  print ("computer_wins is the winner")
elif user_wins > computer_wins:
  print ("user_wins is the winner")
else:
   print("the game is over")
