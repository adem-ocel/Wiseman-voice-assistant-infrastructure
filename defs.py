import speaker
import voice_recognizer

def lissen():
    speaker.play_sound("voices/lissening.mp3")
    voice_recognizer.record(5,"voice.vaw")
    command = voice_recognizer.recognize("voice.vaw").lower()
    if command != "":

        #call your commands
        if command == "hello":hello()
        else:unkowncommand()



#create commands in here.
def hello():
    speaker.speak("hello how can i help you")
    lissen()

def unkowncommand():
    speaker.speak("I dont understand please repeat")
    lissen()