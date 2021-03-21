import cv2
from deepface import DeepFace
import json

# 1. call build model
# 2. Call capture emotion

models = {}

def buildModel():
    # Clears data
    open('data.txt', 'w').close()
    actions = ['Gender','Emotion']
    for action in actions:
        models[action.lower()] = DeepFace.build_model(action)

def classifyEmotion(img):
    obj = DeepFace.analyze(img, models=models, enforce_detection=False)
    return obj['emotion']

def captureEmotion():
    # define a video capture object
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    ret, frame = cap.read()
    cap.release()
    result = classifyEmotion(frame)
    writeResults(result)
    return result


def writeResults(results):
    f = open("data.txt", "a")
    f.write(json.dumps(results))
    f.write("\n")

    #TODO- make a task that captures performance alongside emotions
    #      implement into flask app
    #      Connect to robot response from other computer
    #      Create response strings for introverted, extroverted and moods.
    #      Program basic robot movements/ language