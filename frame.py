# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:48:41 2022

@author: s27jh
"""

import cv2
import os
#from lip_landmark import lip_detection

# Speaker becomes folder
def get_frame(sec, vid_cap, folder, path, file, count):
    file = file.replace('.align', '')
    vid_cap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
    has_frames, image = vid_cap.read()
    if has_frames:
        file_name = os.path.join(path, str(folder) + "_" + file + str(count) + ".jpg")
        # lip_detection(image, file_name)
        try:
            cv2.imwrite(file_name, image)  # save frame as JPG file
        except:
            pass
    return has_frames


def text_annotation(file, speaker_name):
    path = "lab" + "/" + speaker_name + "/" + file
    text = open(path, "r")
    lines = text.readlines()
    end = []
    word = []
    for line in lines:
        words = line.split()
        end.append(int(words[1]) // 1000)
        word.append(words[2])
    return word, end

    # Speaker folder becomes Speaker and then becomes Speaker_name
def load_video_from_folder(root, speaker):
    fold_name = root + "/" + speaker
    for file in os.listdir(fold_name):
        file_name = fold_name + "/" + file
        vid_cap = cv2.VideoCapture(file_name)

        file = file.replace('.mp4', '.lab')
        sentence = file.replace('.lab', '')
        words, end = text_annotation(file, speaker)
        words[0] = "sil_start"
        words[-1] = "sil_end"
        text_path = "C:\\Users\\s27jh\\OneDrive\\Desktop\\Lab_Sequence" + "/"

        threshold = end[0]
        word = words[0]
        text_path += word + "/" + speaker
        sen_len = len(words)
        print(words)
        print(end)
        try:
            os.mkdir(os.path.join(text_path, sentence))
        except OSError as err:
            print(end="")

        img_path = text_path + "/" + sentence
        print(img_path)
        out = [words[i] + " " + str(end[i]) for i in range(sen_len - 1)]
        print(out)
        # print("\n")
        sec = 0
        frame_rate = 0.04  # //it will capture image in each 0.04 second
        count = 0
        num = 0
        success = get_frame(sec, vid_cap, speaker, img_path, file, count)
        while success:

            if count >= threshold:
                num += 1
                if num == sen_len:
                    break
                threshold = end[num]
                word = words[num]
                # text_path = text_path.replace(words[num - 1], word)
                text_path = "frame_sequence" + "/" + word + "/" + speaker
                try:
                    os.makedirs(os.path.join(text_path, sentence))
                except OSError as err:
                    print(end="")
                img_path = text_path + "/" + sentence
                print(img_path)
            sec = sec + frame_rate
            sec = round(sec, 2)
            success = get_frame(sec, vid_cap, speaker, img_path, file, count)
            count += 1



root_folder = "C:\\Users\\s27jh\\OneDrive\\Desktop\\Video_Sequence"

for speaker_folder in os.listdir(root_folder):
    #load_video_from_folder(root_folder, speaker_folder)
    print(speaker_folder)