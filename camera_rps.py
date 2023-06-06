import cv2
from keras.models import load_model
import numpy as np
import time
import random
cap = cv2.VideoCapture(0)

list1 = ["rock","paper","scissors","nothing"]
def get_prediction():
  model = load_model('keras_model.h5')
  cap = cv2.VideoCapture(0)
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  start_time = time.time()
  while time.time() < start_time+10: 
    count_down = str(int(start_time+10-time.time()))
    #print(count_down)
    ret, frame = cap.read()

    # frame_test= np.array(frame)
    # frame_test.shape                 #to find the dimension of your webcam
    # print(frame_test.shape)
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    prediction = list1[np.argmax(prediction)]
    cv2.putText(frame, "User_choice",(50,50),cv2.FONT_HERSHEY_PLAIN,5,(255,50,50),4)
    cv2.putText(frame, count_down,(150,150),cv2.FONT_HERSHEY_PLAIN,5,(255,50,50),4)
    cv2.imshow('frame', frame)
    # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    # cv2.imshow('frame',gray)
    # Press q to close the window 
   # print('pred = ', prediction)
    if cv2.waitKey(30) & 0xFF == ord('q'):
      break
  # cv2.imshow()

  cap.release()
  # Destroy all the windows
  cv2.destroyAllWindows()
  return prediction

def get_winner(computer_choice , user_choice):
  computer_wins = 0
  user_wins= 0
  rounds_played = 0

  while True:
    if computer_wins <3 and user_wins <3:
      #ret, frame = cap.read()
      computer_choice = random.choice(list1)
      print('comp = ', computer_choice)
      user_choice = get_prediction()
      print('usr = ', user_choice, 'comp = ', computer_choice)
      cv2.putText(frame, f'{user_choice}- {computer_choice}',(50,50),cv2.FONT_HERSHEY_PLAIN,5,(255,50,50),4)
      rounds_played +=1
      if computer_choice == user_choice:
        print("It is a tie!")
        winner = "tie"
      elif (computer_choice == "rock"and user_choice == "scissors") or (computer_choice == "paper" and user_choice == "rock") or (computer_choice == "scissors"and user_choice == "paper"):
        print("You lost")
        winner = "computer_choice"
        computer_wins +=1
      
      else:
        print("You won!")
        winner = "user_choice"
        user_wins +=1
      
    # return winner
      if computer_wins == 3:
        print("computer is a winner")
      elif user_wins == 3 :
          print("user is a winner")
      else:
          print("The game is over")


get_winner('computer_choice' , 'user_choice')
get_prediction()





