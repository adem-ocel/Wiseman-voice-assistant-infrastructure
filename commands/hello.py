import sys
import os
sys.path.append(os.path.dirname(__file__)+"/..")
import defs 
aliases =[
"hello",
"hi",
]

with open(os.path.dirname(__file__)+"/command", "r") as commandfile:
    command = commandfile.read()
    if command in aliases:
        
        import speaker
        speaker.speak("hello how can i help you")
        defs.lissen()
