import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

# #face recognition
# models = ['DeepFace']
# for model_name in models:
#    model = DeepFace.build_model(model_name)

#facial analysis
models = {}
actions = ['Age', 'Gender', 'Emotion', 'Race']
for action in actions:
   models[action.lower()] = DeepFace.build_model(action)
obj=DeepFace.analyze("../database/Girl.jpeg", models=models, enforce_detection=False)
print(obj['emotion'])




import numpy as np

# img = cv2.imread('HappyBoy.jpg')
# img = np.real(img)

# # plt.imshow(img, cv2.COLOR_BGR2RGB)
#
#
# # plt.interactive(False)
# # plt.imshow('HappyBoy.jpg')
#
# # plt.figure("Comparision")
# # plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# # plt.show()
# prediction = DeepFace.verify('HappyBoy.jpg', enforce_detection=False)
# print(prediction)
# # print(prediction)

from deepface import DeepFace
# result = DeepFace.verify('HappyBoy.jpg', enforce_detection=False)
#results = DeepFace.verify([['img1.jpg', 'img2.jpg'], ['img1.jpg', 'img3.jpg']])
# print("Is verified: ", prediction["verified"])