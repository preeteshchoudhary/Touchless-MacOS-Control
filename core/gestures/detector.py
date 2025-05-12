import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import os
import threading

class GestureDetector:
    def __init__(self, model_path=os.path.abspath('gesture_recognizer.task')):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file missing: {model_path}")
            
        # MediaPipe setup
        self.base_options = python.BaseOptions(model_asset_path=model_path)
        self.options = vision.GestureRecognizerOptions(
            base_options=self.base_options,
            running_mode=vision.RunningMode.LIVE_STREAM,
            result_callback=self._gesture_callback
        )
        self.recognizer = vision.GestureRecognizer.create_from_options(self.options)
        
        # Video capture
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("Failed to open camera")
            
        # State management
        self.latest_gesture = None
        self.prev_gesture = None  # Track previous gesture
        self.latest_frame = None
        self.timestamp = 0
        self.lock = threading.Lock()
        self.running = True

        # Start processing thread
        self.processing_thread = threading.Thread(target=self._process_frames, daemon=True)
        self.processing_thread.start()

    def _gesture_callback(self, result, output_image, timestamp_ms):
        """Async callback for gesture results"""
        with self.lock:
            if result.gestures:
                self.latest_gesture = result.gestures[0][0].category_name

    def _process_frames(self):
        """Dedicated thread for frame processing"""
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            # Store latest frame for preview
            with self.lock:
                self.latest_frame = frame.copy()

            # Convert to MediaPipe format
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            
            # Process asynchronously
            try:
                self.recognizer.recognize_async(mp_image, self.timestamp)
                self.timestamp += 1
            except Exception as e:
                print(f"Processing error: {e}")

    def get_gesture(self):
        """Thread-safe way to get latest gesture (resets after retrieval)"""
        with self.lock:
            current_gesture = self.latest_gesture
            if current_gesture != self.prev_gesture:
                self.prev_gesture = current_gesture
                self.latest_gesture = None  # Reset after retrieval
                return current_gesture
            return None

    def get_frame(self):
        """Get latest frame for preview"""
        with self.lock:
            if self.latest_frame is not None:
                return True, self.latest_frame.copy()
            return False, None

    def stop(self):
        """Cleanup resources"""
        self.running = False
        self.cap.release()
        self.recognizer.close()
