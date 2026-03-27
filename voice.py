import whisper
import sounddevice as sd
import numpy as np
import pyttsx3


class Voice:

    def __init__(self):

        # Better model for accuracy
        self.model = whisper.load_model("small")

        self.engine = pyttsx3.init()

        self.sample_rate = 16000

    def listen(self):

        print("Listening...")

        duration = 6  # increased to allow natural speech
        recording = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype='float32'
        )

        sd.wait()

        audio = np.squeeze(recording)

        # Whisper with VAD + noise filtering
        result = self.model.transcribe(
            audio,
            vad_filter=True,
            no_speech_threshold=0.6
        )

        text = result["text"].strip()

        # 🚫 Reject garbage / hallucinations
        if not text or len(text) < 3:
            return ""

        garbage = ["you", "thanks", "thank you", ".", "..."]
        if text.lower() in garbage:
            return ""

        print("Heard:", text)

        return text

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()