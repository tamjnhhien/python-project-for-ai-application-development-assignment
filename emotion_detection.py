from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions

def emotion_predictor(text):
    if not text.strip():  # Check if the text is empty or just whitespace
        return {"error": "No text provided"}  # Return a 400 status code with an error message
    
    # Use IamAuthenticator to authenticate using the API key
    API_KEY = 'Jg4n5spjBP916fmiQRmlVkXivOwhMjqaSt2YqLxEWRmp'
    URL = 'https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/a434082c-6277-4a50-92c6-198d09b46434'
    nlu = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
		authenticator=IAMAuthenticator(API_KEY)
    )

    nlu.set_service_url(URL)

    # Call the Watson NLU service to analyze emotions
    response = nlu.analyze(
        text=text,
        features=Features(emotion=EmotionOptions())
    ).get_result()

    # Return the emotion analysis results
    emotions = response['emotion']['document']
    return {"emotion": emotions, "text": text}
    
