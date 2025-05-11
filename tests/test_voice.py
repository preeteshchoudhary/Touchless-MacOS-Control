import unittest
from core.voice.listener import VoiceListener

class TestVoiceListener(unittest.TestCase):
    def setUp(self):
        self.listener = VoiceListener()

    def test_listen_no_voice(self):
        # Placeholder: test with no voice input
        result = self.listener.listen()
        self.assertIsNone(result)

    # Add more tests as you implement logic

if __name__ == '__main__':
    unittest.main()
