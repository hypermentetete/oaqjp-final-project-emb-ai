from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        r = emotion_detector('I am glad this happened')
        self.assertEqual(r['dominant_emotion'], 'joy')
        r = emotion_detector('I am really mad about this')
        self.assertEqual(r['dominant_emotion'], 'anger')
        r = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(r['dominant_emotion'], 'disgust')
        r = emotion_detector('I am so sad about this')
        self.assertEqual(r['dominant_emotion'], 'sadness')
        r = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(r['dominant_emotion'], 'fear')

unittest.main()
