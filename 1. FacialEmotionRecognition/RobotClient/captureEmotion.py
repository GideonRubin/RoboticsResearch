import os

import cv2
from deepface import DeepFace
import json
from multiprocessing import Process, Queue

# 1. call build model
# 2. Call capture emotion

models = {}
done = False
file = 'data.json'

def buildModel():
    # Clears data formats start of json array
    f=open(file, 'w')
    f.write("[")

    # Uncomment to build based on a chosen model
    # DeepFace.build_model(model_name='DeepFace')


def classifyEmotion(img):
    obj = DeepFace.analyze(img, actions=['emotion'], models=models, enforce_detection=False)
    return obj

# Writes all emotions to file, returns dominant emotion
def captureEmotion():
    # define a video capture object
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    ret, frame = cap.read()
    cap.release()

    cv2.imwrite("image.png", frame)
    result = classifyEmotion(cv2.imread("image.png"))
    writeResultsToFile(result['emotion'])

    return result['dominant_emotion']


def writeResultsToFile(results):
    f = open(file, "a")
    f.write(json.dumps(results))
    if done == False:
        f.write(",")
        f.write("\n")
    else:
        f.write("]")

## Need to test this:
# def generateReport():
#     emotion = {
#         "angry": 0,
#         "disgust": 0,
#         "fear": 0,
#         "happy": 0,
#         "sad": 0,
#         "surprise": 0,
#         "neutral": 0
#     }
#     with open(file, 'r') as f:
#         emotions = json.load(f)
#     for x in emotions:
#         for y in emotions[x]:
#             emotion[y] += emotions[y]
#     for x in emotion:
#         emotion[x] /= len(emotions)
#     with open('summary', 'w') as s:
#         s.write(json.dumps(emotion))

    # f.write("]")
    # print(f)


