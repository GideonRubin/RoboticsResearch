from naoqi import ALProxy
import pyttsx3 #Optional

port=51008
def sayAndSend(myVal):
    # Uses native text to speech to simulate for virtual NAO
    engine = pyttsx3.init()
    engine.say(myVal)
    engine.runAndWait()
    #Sends the value to Choregraphe
    tts = ALProxy("ALTextToSpeech", "127.0.0.2", port)
    tts.say(myVal)
    engine.stop()

def say(myVal):
    # Uses native text to speech to simulate for virtual NAO
    engine = pyttsx3.init()
    engine.say(myVal)
    engine.runAndWait()

# port = int(input("Enter your port here: "))
# sayAndSend("Hello World!")
#
#
