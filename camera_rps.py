import cv2
from keras.models import load_model
import numpy as np
import time
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
    cv2.imshow('frame', frame)
    # Press q to close the window 
    print(prediction)
    if cv2.waitKey(10) & 0xFF == ord('q'):
      break
  cap.release()
  # Destroy all the windows
  cv2.destroyAllWindows()
  return prediction


list1 = ["rock","paper","scissors","nothing"]

t1 = get_prediction()
print(t1)
# cv2.imshow()


