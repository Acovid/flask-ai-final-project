from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def em_detect():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    # label = response['label']
    # score = response['score']

    # Return a formatted string with the sentiment label and score
    # return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)    
    return response