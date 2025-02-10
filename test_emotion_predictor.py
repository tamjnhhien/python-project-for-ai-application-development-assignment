import unittest
from emotion_detector import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):

    def test_positive_text(self):
        text = "I am feeling very happy today!"
        result = emotion_predictor(text)

        # Ensure 'emotion' is part of the result
        self.assertIn('emotion', result)

        # Ensure 'emotion' contains the correct nested structure
        self.assertIn('emotion', result['emotion'])  # Check for nested 'emotion'
        self.assertIn('joy', result['emotion']['emotion'])  # Check if 'joy' is part of the emotions
        self.assertIn('sadness', result['emotion']['emotion'])  # Check if 'sadness' is part of the emotions

        # Ensure 'text' is part of the result and matches the input text
        self.assertIn('text', result)
        self.assertEqual(result['text'], text)

    def test_negative_text(self):
        text = "I am feeling very sad today."
        result = emotion_predictor(text)

        # Ensure 'emotion' is part of the result
        self.assertIn('emotion', result)

        # Ensure 'emotion' contains the correct nested structure
        self.assertIn('emotion', result['emotion'])  # Check for nested 'emotion'
        self.assertIn('sadness', result['emotion']['emotion'])  # Check if 'sadness' is part of the emotions

        # Ensure 'text' is part of the result and matches the input text
        self.assertIn('text', result)
        self.assertEqual(result['text'], text)

    def test_empty_text(self):
        text = ""
        result = emotion_predictor(text)
        
        # Check if the result contains the expected error message
        self.assertEqual(result, {"error": "No text provided"})  # Check if error message is returned

if __name__ == '__main__':
    unittest.main()
