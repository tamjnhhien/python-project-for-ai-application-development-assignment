from emotion_detection import emotion_predictor

if __name__ == "__main__":
    text = "I am feeling very happy today!"
    result = emotion_predictor(text)
    print(result)
