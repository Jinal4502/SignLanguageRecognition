# clone repo: done
# collect images - code done
# setup labelImg done
# label images done
# update labelmap done
# train
# update checkpoint
# detect

import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collected-images'

labels = ['A', 'B', 'C', 'D', 'E', 'F']
number_imgs = 15

for label in labels:
    !mkdir {'Tensorflow\workspace\images\collected-images\\' + label}
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path, join(
            IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
        cap.release()
