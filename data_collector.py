# how to collect the data using opencv python

# open the camera and capturing the images 
import os
import cv2
import time
import uuid    # to save the images with unique names

IMAGES_PATH = "CollectedImages"

labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']

number_of_images = 5        # for each label

for label in labels:
    image_path = os.path.join(IMAGES_PATH, label)
    os.makedirs(image_path)

    # open camera
    capture = cv2.VideoCapture(0)  ## 0 for using the default camera
    print(f"Collecting images for {label}")
    time.sleep(4)

    for imgnum in range(number_of_images):
        ret, frame = capture.read()
        imagename = os.path.join(IMAGES_PATH, label, label + "." + str(uuid.uuid1()) + ".jpg")
        cv2.imwrite(imagename, frame)
        cv2.imshow("Frame", frame)
        time.sleep(4)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
