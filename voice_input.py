import sounddevice as sd
import queue
import vosk
import sys
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def get_voice_input():
    model = vosk.Model("vosk-model-small-en-us-0.15")  # Path to your Vosk model
    samplerate = 16000

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("\n🎤 Speak into the microphone (say 'stop' to end)...\n")
        rec = vosk.KaldiRecognizer(model, samplerate)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                if text:
                    print(f"You said: {text}")
                    if "stop" in text.lower():
                        print("Voice input stopped.")
                        break
                    return text
            # If interim results needed, use rec.PartialResult()

        return None
