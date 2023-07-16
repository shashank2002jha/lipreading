# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:58:59 2022

@author: s27jh
"""

# TO run the programe with command line argument enable the argument parser and execute the command
# python3 lip_landmark.py --shape-predictor shape_predictor_68_face_landmarks.dat --image Klrahul.png
from imutils import face_utils
import cv2


# Argument parser only to use in  case of  running via a command line

# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True, help="path to the facial landmark predictor")
# ap.add_argument("-i", "--image", required=True, help="path to the input image")
# args = vars(ap.parse_args())
# print(args["image"])

def lip_detection(file_name, detector, predictor, out_path):
    # reading, resizing, the image and applying the detector model on the image
    image = cv2.imread(file_name)
    image = cv2.resize(image, (1280, 800))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 1)

    # variable for storing  starting coordinate and width and height,  to crop the image
    X, Y, W, H = 0, 0, 0, 0

    for (i, rect) in enumerate(rects):
        # determine the facial landmarks for the face region, then
        # convert the facial landmark (x, y)-coordinates to a NumPy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # coordinate for the maximum and minimum x and y around the lips
        x_min, x_max = list(shape[48]), list(shape[54])
        y_min, y_max = list(shape[52]), list(shape[57])

        x, y = x_min[0], y_min[1]
        w = x_max[0] - x_min[0]
        h = y_max[1] - y_min[1]
        x -= int(0.15 * w)
        y -= int(0.25 * h)
        w += int(0.30 * w)
        h += int(0.50 * h)

        (X, Y, W, H) = (x, y, w, h)

        # Drawing the rectangle around the lips
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # loop over the (x, y)-coordinates for the lip landmarks and draw them on the image
        # for (xi, yi) in shape[48:]:
        #     cv2.circle(image, (xi, yi), 1, (0, 0, 255), -1)

    # using width and height and starting x and y calculating the end point coordinate of the lips
    XX = X + W
    YY = Y + H
    # print(X, Y, XX, YY)

    lips = image[Y:YY, X:XX, :]  # croping the lips from the actual image
    try:
        cv2.imwrite(out_path, lips)  # saving the cropped image
    except:
        pass
    # cv2.imshow("output", lips)  # showing the cropped image
    # cv2.waitKey(0)  # wait foe the 'esc' key for closing the output window
    # cv2.destroyAllWindows()  # destroy all the existing windows
#lip_landmark (1).py
#Displaying lip_landmark (1).py.