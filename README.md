# Robotics Research
Research in simulating robots in virtual environments

## Getting started with a simulated Nao in Choregraphe

1. Download the latest version from Windows (only available in 32-bit).
2. Download Python 2.7 SDK 2.5.5 Win 32 Binaries, and unzip the file into C:\pynaoqi. Then go to My Computer > Properties > Advanced System Settings > Environment Variables again, and under System variables, add a new user variable PYTHONPATH and set it as the path\to\python-sdk\lib (e.g., C:\pynaoqi\lib).
3. Open / run the simulated robot as directed in the [documentation](http://doc.aldebaran.com/2-4/software/choregraphe/connection_widget.html#choregraphe-howto-connect-to-simulated-nao)
4. Select the virtual NAO robot: 
  -in the Connection to panel:
  -if the simulated robot appears in the list, double click it,
  -if not, set the IP address to 127.0.0.1 and for the port, search for it in preferences (it should appear under the virtual robot sub menu down the bottom) and click    the Select button.
5. Once you have selected the NAO virtual robot, click connect.


## Connecting the virtual robot with the sdk

Code is available in NaoChat.py in the Getting Started folder.
1. Test that the sdk can talk to the virtual robot by running the following code and looking at the:
``
from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "<IP of your robot>", <Port of your robot (integer)>)
tts.say("Hello, world!")
``
2. See above (step 4) for checking the port and IP. 
3. The virtual robot speech should appear as a bubble in the robot view (the virtual robot can't produce sound or show LED lights, it also has maximal stiffness).


## Connecting the laptop webcam with the virtual NAO robot using SDK and Choregraphe

Code is available in NaoWebcam.py in the Getting Started folder.
1. Install open-cv (because the sdk is for python 2.7 32-bit, I used ``pip2 install opencv-python==4.2.0.32``).
2. This should install numpy, if not, install as well.
3. Run the python file and verify that the data is being seen in the webcam view in Choregraphe.
