import unittest
from core.gestures.detector import GestureDetector

class TestGestureDetector(unittest.TestCase):
    def setUp(self):
        self.detector = GestureDetector()

    def test_detect_no_hand(self):
        # Placeholder: test with no hand in frame
        self.assertIsNone(self.detector.detect())

    # Add more tests as you implement detection logic

if __name__ == '__main__':
    unittest.main()
