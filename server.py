"""
    Analyzes emotions in the text provided by the user.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Renders the index.html page when the root URL ("/") is accessed.

    Returns:
    str: The rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Handles GET requests to analyze the emotional content of a given text.

    Retrieves the text input from the request arguments and passes it to 
    the `emotion_detector` function to analyze its emotional content.

    Returns:
    - If the API returns a valid response, a dictionary containing emotion scores 
      (anger, disgust, fear, joy, sadness) and the dominant emotion.
    - If the input text is invalid, returns an error message.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a dictionary with emotions
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
