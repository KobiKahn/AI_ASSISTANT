import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import time

# TEST 1

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file

try:
    time.sleep(5)
    speech_file = 'output.wav'

    r = sr.Recognizer()

    with sr.AudioFile(speech_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        print(text)

except:
    print("An Error Occured")