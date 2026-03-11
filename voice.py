import whisper
import sounddevice as sd
import numpy as np
import pyttsx3

class Voice:

    def __init__(self):

        self.model = whisper.load_model("base")

        self.engine = pyttsx3.init()

    def listen(self):

        print("Listening...")

        duration = 5
        samplerate = 16000

        recording = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype='float32'
        )

        sd.wait()

        audio = np.squeeze(recording)

        result = self.model.transcribe(audio)

        text = result["text"]

        print("Heard:", text)

        return text

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()