import speech_recognition as sr
import queue
import threading
import time

class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.audio_queue = queue.Queue()
        self.stop_event = threading.Event()
        self.listener_thread = None
        self.retry_delay = 2

    def _background_listen(self):
        while not self.stop_event.is_set():
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=1)
                    print("Calibrated. Listening...")
                    while not self.stop_event.is_set():
                        try:
                            audio = self.recognizer.listen(
                                source, 
                                timeout=1.5,
                                phrase_time_limit=1
                            )
                            text = self.recognizer.recognize_google(audio)
                            self.audio_queue.put(text.lower())
                            print(f"Heard: {text}")
                        except sr.WaitTimeoutError:
                            continue
                        except sr.UnknownValueError:
                            print("Audio unclear - try speaking closer")
                        except sr.RequestError as e:
                            print(f"Google API error: {e}")
                            time.sleep(self.retry_delay)
                        except ConnectionResetError:
                            print("Connection reset - retrying...")
                            time.sleep(self.retry_delay)
                            self._reinitialize_microphone()
            except OSError as e:
                print(f"Microphone error: {e}")
                time.sleep(5)
                self._reinitialize_microphone()

    def _reinitialize_microphone(self):
        self.microphone = sr.Microphone()
        print("Microphone reinitialized")

    def start(self):
        self.listener_thread = threading.Thread(target=self._background_listen, daemon=True)
        self.listener_thread.start()

    def listen(self):
        return self.audio_queue.get() if not self.audio_queue.empty() else None

    def stop(self):
        self.stop_event.set()
        if self.listener_thread:
            self.listener_thread.join()
