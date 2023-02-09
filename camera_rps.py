import cv2
from keras.models import load_model
import numpy as np
import time
import random
list1 = ["rock","paper","scissors","nothing"]
def get_prediction():
  model = load_model('keras_model.h5')
  cap = cv2.VideoCapture(0)
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  start_time = time.time()
  while time.time() < start_time+4: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    prediction = list1[np.argmax(prediction)]
    cv2.imshow('frame', frame)
    # Press q to close the window 
    print(prediction)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
  cap.release()
  # Destroy all the windows
  cv2.destroyAllWindows()
  return prediction

computer_wins = 0
user_wins= 0
rounds_played = 0

def get_winner(computer_choice , user_choice):
  while computer_wins <3 and user_wins <3:
    
    computer_choice = random.choice(list1[:3])
    print(computer_choice)
    user_choice = get_prediction()
    print(user_choice)
    rounds_played +=1
    if computer_choice == user_choice:
      print("It is a tie!")
      winner = "tie"
    elif (computer_choice == "Rock"and user_choice == "Scissors") or (computer_choice == "Paper" and user_choice == "Rock") or (computer_choice == "Scissors"and user_choice == "Paper"):
      print("You lost")
      winner = "computer_choice"
      computer_wins +=1
    
    else:
      print("You won!")
      winner = "user_choice"
      user_wins +=1
      
    # return winner
  if computer_wins > user_wins:
     print(computer_wins, "is a winner")
  elif user_wins > computer_wins:
      print(user_wins, "is a winner")
  else:
      print("The game is over")


get_winner()

# cv2.imshow()


