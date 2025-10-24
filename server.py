''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detection():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows values of basic emojis 
        and dominant emoji of the provided text.
    '''
    text_to_analyse = str(request.args.get("textToAnalyze"))
    # if not len(text_to_analyse):
    #     return "Imput shouldn't be empty!"
    emotions = emotion_detector(text_to_analyse)
    anger = emotions["anger"]
    sadness = emotions["sadness"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    dominant_emotion = emotions["dominant_emotion"]
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is 'anger': {anger},
    'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. 
    The dominant emotion is {dominant_emotion}."""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
