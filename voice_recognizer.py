import speech_recognition as sr
import pyaudio
import wave
from termcolor import colored
import settings

tanima_motoru = sr.Recognizer()

def recognize(voice):
    with sr.AudioFile(voice) as kaynak:
        ses = tanima_motoru.record(kaynak)
        try:
            text = tanima_motoru.recognize_google(ses, language=settings.lang) 
            print(colored(f"{settings.username}: {text}",settings.user_console_color))
            return text
        except sr.UnknownValueError:
            print(colored(f"unkown value err.",settings.recognize_error_color))
            return ""
        except sr.RequestError as e:
            print(colored(f"request err.",settings.recognize_error_color))
            return ""


def record(sure, dosya_adi):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = sure

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        frames.append(stream.read(CHUNK))

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(dosya_adi, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
