import whisper
import sounddevice as sd
import numpy as np
import pyttsx3
import queue


class Voice:

    def __init__(self):

        self.model = whisper.load_model("small")
        self.engine = pyttsx3.init()

        self.sample_rate = 16000
        self.energy_threshold = 0.01

        self.q = queue.Queue()

    # 🔊 Audio callback (non-blocking, real-time)
    def callback(self, indata, frames, time, status):
        if status:
            return
        self.q.put(indata.copy())

    def listen(self):

        print("Listening...")

        recording = []
        silence_counter = 0
        started = False

        with sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            dtype='float32',
            callback=self.callback
        ):

            while True:

                audio_chunk = self.q.get()
                volume = np.linalg.norm(audio_chunk)

                # 🎤 Start when speech detected
                if volume > self.energy_threshold:
                    started = True
                    recording.append(audio_chunk)
                    silence_counter = 0

                elif started:
                    recording.append(audio_chunk)
                    silence_counter += 1

                # 🛑 Stop after silence (~1 sec)
                if started and silence_counter > 20:
                    break

        if not recording:
            return ""

        audio = np.concatenate(recording, axis=0)
        audio = np.squeeze(audio)

        # 🔥 Normalize audio
        max_val = np.max(np.abs(audio))
        if max_val > 0:
            audio = audio / max_val

        # 🔥 Transcribe (deterministic)
        result = self.model.transcribe(
            audio,
            temperature=0.0,
            beam_size=5,
            best_of=1
        )

        text = result["text"].strip()

        # 🚫 Filter garbage
        if not text or len(text) < 3:
            return ""

        # 🚫 Filter hallucinated loops
        if len(text) > 150:
            return ""

        if text.count("thank you") > 2:
            return ""

        garbage = ["you", "thanks", "thank you", ".", "..."]
        if text.lower() in garbage:
            return ""

        print("Heard:", text)

        return text

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()