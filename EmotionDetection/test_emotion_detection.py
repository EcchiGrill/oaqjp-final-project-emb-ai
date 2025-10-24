import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_dominant_joy(self):
        response = emotion_detector('I am glad this happened')
        self.assertEqual(response['dominant_emotion'], 'joy')

    def test_dominant_anger(self):
        response = emotion_detector('I am really mad about this')
        self.assertEqual(response['dominant_emotion'], 'anger')
    
    def test_dominant_disgust(self):
        response = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(response['dominant_emotion'], 'disgust')

    def test_dominant_sadness(self):
        response = emotion_detector('I am so sad about this')
        self.assertEqual(response['dominant_emotion'], 'sadness')

    def test_dominant_fear(self):
        response = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(response['dominant_emotion'], 'fear')

unittest.main()