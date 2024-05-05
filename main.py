import voice_recognizer
import settings
import defs
while 1:
    voice_recognizer.record(2,"voice.vaw")
    text = voice_recognizer.recognize("voice.vaw")
    if settings.botname in text:
        defs.lissen()