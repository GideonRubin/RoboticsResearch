import cv2
from naoqi import ALProxy
import vision_definitions
import time

ip = '127.0.0.1'
port = int(input('Enter the port: '))

if ip=='':
    ip='127.0.0.1'
if port=='':
    port=9559

camProxy = ALProxy("ALVideoDevice", ip,port)

vc = cv2.VideoCapture(0)
print(camProxy.getExpectedImageParameters(0))
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while vc.isOpened():
    rval, frame = vc.read()
    frame=cv2.resize(frame, (640, 480))
    time.sleep(0.15)
    b,g,r = cv2.split(frame)       # get b,g,r
    rgb_img = cv2.merge([r,g,b])     # switch it to rgb
	#important: image sent to the robot upper camera is rgb 640x480 
    set=camProxy.putImage(0,640,480,rgb_img.tobytes())
    # print(set)
camProxy.unsubscribe(camProxy)
cv2.destroyWindow("preview")

