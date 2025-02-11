import requests # Import the requests library to handle HTTP requests
import json

# Function takes a string input that should be analysed
def emotion_detector(text_to_analyze):
    
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create a dictionary with the text to be analysed
    myobj = {"raw_document": { "text": text_to_analyze }}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=headers)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotions_with_scores = {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score}

    # Find the key with the highest value
    max_key = max(emotions_with_scores, key=emotions_with_scores.get)
    # Add 'dominant_emotion' to the dictionary
    emotions_with_scores['dominant_emotion'] = max_key
   
    return   emotions_with_scores    
