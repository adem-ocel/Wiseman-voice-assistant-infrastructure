import speaker
import voice_recognizer
import speaker
import os
import glob
def lissen():
    speaker.play_sound("voices/lissening.mp3")
    voice_recognizer.record(5,"voice.vaw")
    
    command = voice_recognizer.recognize("voice.vaw").lower()
    with open(os.path.dirname(__file__)+"/commands/command", "w") as commandfile:
         commandfile.write(command)

    command_files = glob.glob(os.path.join("commands", '*.py'))
    for commandfile in command_files:
        os.system('python {}'.format(commandfile))
