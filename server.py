from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Return a dictionary with emotions
    if response["dominant_emotion"] == None:
        return "Invalid text! Please try again!"
    else:
        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)