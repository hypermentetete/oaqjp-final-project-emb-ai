from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def call_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    r = emotion_detector(text_to_analyze)
    if r['dominant_emotion'] == 'None':
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {r['anger']}, " \
            f"'disgust': {r['disgust']}, " \
            f"'fear': {r['fear']}, " \
            f"'joy': {r['joy']}, " \
            f"'sadness': {r['sadness']}. " \
            f"The dominant emotion is {r['dominant_emotion']}. "

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
