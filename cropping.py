# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 23:30:44 2022

@author: s27jh
"""

import os
from lip_landmark import lip_detection
import dlib
import time

start = time.time()
# loading the detector of dlib and pretrained model
detector = dlib.get_frontal_face_detector()
model_path = './detection_model/shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(model_path)

root_path = "frame_sequence"
output_folder = "lip_sequence"
try:
    os.mkdir(output_folder)
except:
    pass

for word in os.listdir(root_path):
    path = root_path + "/" + word
    directory=os.path.join(output_folder, word)
    if not os.path.exists(directory):
            os.makedirs(directory)
    #os.mkdir(os.path.join(output_folder, word))
    link = output_folder + "/" + word
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+                ", word, ",  is starting                         +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for speaker in os.listdir(path):
        path1 = path + "/" + speaker
        directory=os.path.join(link, speaker)
        if not os.path.exists(directory):
            os.makedirs(directory)
        #os.mkdir(os.path.join(link, speaker))
        link1 = link + "/" + speaker
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("+                ", speaker, ",  is starting                      +")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        for sentence in os.listdir(path1):
            print(sentence, " is starting", end="\n ")
            path11 = path1 + "/" + sentence
            directory=os.path.join(link1, sentence)
            if not os.path.exists(directory):
                os.mkdir(os.path.join(link1, sentence))
            else:
                continue
            link11 = link1 + "/" + sentence
            for file in os.listdir(path11):
                img_path = path11 + "/" + file
                out_path = link11 + "/" + file
                lip_detection(img_path, detector, predictor, out_path)
            print(word, speaker, sentence + " is complete", end="\n\n")
        print(speaker, " is complete", end="\n")
        print("------------------------------------------------------------")
    print(word, " is complete", end="\n")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

time.sleep(1)
end = time.time() - start
print("Time taken by prgramme to run is : {0:.3f}".format(end))
