# Computer Vision RPS
## Milestone 1: Set Up the Environment!
 In this Milestone, we have made a folder called computer-vision and connected it to the git hub. 


## Milestone 2: Create the computer version:
In this Milestone we have made a use of websit called Teachable Machine. 
Click here :
[https://teachablemachine.withgoogle.com/]

Go to Teachable-Machine  to start creating the model. Each class is trained with images of yourself showing each option to the camera. The "Nothing" class represents the lack of option in the image. Remember that the more images you train with, the more accurate the model will be.
Download the model from the "Tensorflow" tab in Teachable-Machine. The model should be named keras_model.h5 and the text file containing the labels should be named labels.txt.

The files you are downloading contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. Later, you will load them into your Python application in the next milestone.

Make sure you push the model and labels to your GitHub repository after committing.

## Milestone 3: Install the Dependencies:
---
## Task 1 :
Before you can use the model, you need to install the libraries that it depends on.

Create a conda environment and then install the necessary requirements. You need **opencv-python, tensorflow, and ipykernel**. Start by creating the environment, activate it, and then install pip by running the following command in your terminal conda install pip. Then, to install the rest of the libraries, run pip install **library**

## **Important**: If you are on Ubuntu, the latest version of Tensorflow doens't work with the default version of Python. When creating the virtual environment, use Python 3.8 instead by running:

**conda create -n my_env python=3.8**

Where my_env is the name of the environment you want to create.
After that, the libraries you have to install are the ones mentioned above.
***
## Task2: 
## Are you on a Mac with an M1 chip?
Install Miniconda. First, create a virtual environment by running the following commands:

***conda create -n tensorflow-env python=3.9***

***conda activate tensorflow-env***

***conda install pip***

Then, follow the steps from the section that says "arm64: Apple Silicon" from this link.
Once you get tensorflow for Mac, you will install opencv for Mac by running the following commands:

***conda install -c conda-forge opencv***
***
## Task3 : Complete the installation of dependencies
Finally, make sure you install ipykernel by running the following command:

***pip install ipykernel***

Once you installed everything (regardless of the operating system) create a requirements.txt file by running the following command:

**pip list > requirements.txt**
***
## Task4: Check the model is working
To ensure your model is working first download this file 
click here 

[https://aicore-files.s3.amazonaws.com/Foundations/Python_Programming/RPS-Template.py]

once done make sure that you have the correct name for the model, the correct name for the labels, and that the model and this file are in the same folder
***
## Milestone 4: Create a Rock-Paper-Scissor-Game
This code needs to randomly choose an option (rock, paper, or scissors) and then ask the user for an input.Create another file called manual_rps.py that will be used to play the game without the camera.You will need to use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

Create two functions: get_computer_choice and get_user_choice.
The first function will randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice.The second function will ask the user for an input and return it.

Wrap the code in a function called get_winner and return the winner.This function takes two arguments: computer_choice and user_choice.If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".
Create and call a new function called play.Inside the function you will call all the other three functions you've created (get_computer_choice, get_user_choice, and get_winner)
.Now when you run the code, it should play a game of Rock-Paper-Scissors, and it should print whether the computer or you won.
```
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
  elif (computer_choice == "Rock"and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors"and user_choice == "Paper"):
    print("You lost")
    winner = "computer_choice"
  else:
    print("You won!")
    winner = "user_choice"
  return winner

def play():
  t1= get_computer_choice()
  print(t1)
  t2= get_user_choice()
  print(t2)
  t3= get_winner(t1,t2)
  print(t3)

play()

```
**Test the code and see who wins!!!**
***
## Milestone 5
Replace the hard-coded user guess with the output of the computer vision model. Create a new file called camera_rps.py where you will write the new code.

Create a new function called get_prediction that will return the output of the model you used earlier.

Remember that the output of the model you downloaded is a list of probabilities for each class. You need to pick the class with the highest probability. So, for example, assuming you trained the model in this order: "Rock", "Paper", "Scissors", and "Nothing", if the first element of the list is 0.8, the second element is 0.1, the third element is 0.05, and the fourth element is 0.05, then, the model predicts that you showed "Rock" to the camera with a confidence of 0.8.

The model can make many predictions at once if given many images. In your case you only give it one image at a time. That means that the first element in the list returned from the model is a list of probabilities for the four different classes. Print the response of the model if you are unclear of this.
```
```
Thank you !!!

![flower image](C:\Intel\my_folder\computer-vision-rock-paper-scissors\RGB_image1.jpg)


