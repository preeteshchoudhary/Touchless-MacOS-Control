from core.gestures.detector import GestureDetector
from core.gestures.mapper import GestureMapper
from core.voice.listener import VoiceListener
from core.voice.verifier import SpeakerVerifier
from core.system.actions import SystemActions
import threading
import time
import queue
import cv2

class MainController:
    def __init__(self):
        self.gesture_detector = GestureDetector()
        self.voice_listener = VoiceListener()
        self.gesture_mapper = GestureMapper()
        self.voice_mapper = GestureMapper('config/voice_commands.yaml')
        self.system_actions = SystemActions()
        self.speaker_verifier = SpeakerVerifier()
        self.frame_lock = threading.Lock()
        self.running = True
        self.gesture_queue = queue.Queue()
        self.voice_queue = queue.Queue()

    def start(self):
        threading.Thread(target=self._gesture_worker, daemon=True).start()
        self.voice_listener.start()
        self._video_preview_worker()
        
        print("System ready. Use gestures or voice commands. Press Ctrl+C to exit.")
        try:
            while self.running:
                self._process_gestures()
                self._process_voice()
                time.sleep(0.05)
        except KeyboardInterrupt:
            self.stop()

    def _gesture_worker(self):
        while self.running:
            gesture = self.gesture_detector.get_gesture()
            if gesture:
                self.gesture_queue.put(gesture)
            time.sleep(0.1)

    def _video_preview_worker(self):
        cv2.namedWindow('Gesture Detection')
        while self.running:
            try:
                with self.frame_lock:
                    ret, frame = self.gesture_detector.get_frame()
                if ret:
                    cv2.imshow('Gesture Detection', frame)
                    if cv2.pollKey(1) & 0xFF == ord('q'):
                        break
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Video error: {e}")
                break
        cv2.destroyAllWindows()

    def _process_gestures(self):
        while not self.gesture_queue.empty():
            gesture = self.gesture_queue.get()
            action = self.gesture_mapper.map_gesture(gesture)
            if action:
                self.system_actions.execute(action)
                print(f"Gesture: {gesture} → {action}")

    def _process_voice(self):
        command = self.voice_listener.listen()
        if command:
            action = self.voice_mapper.map_gesture(command)
            if action and self.speaker_verifier.verify():
                self.system_actions.execute(action)
                print(f"Voice: {command} → {action}")

    def stop(self):
        self.running = False
        self.voice_listener.stop()
        self.gesture_detector.stop()
        with self.frame_lock:
            cv2.destroyAllWindows()
        print("\nSystem shut down cleanly")

if __name__ == "__main__":
    controller = MainController()
    controller.start()
