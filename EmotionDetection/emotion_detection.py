import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    r = requests.post(url, json = myobj, headers=header)
    if r.status_code == 400:
        return {'anger': 'None',
                'disgust': 'None',
                'fear': 'None',
                'joy': 'None',
                'sadness': 'None',
                'dominant_emotion': 'None'}
    fr = json.loads(r.text)
    dominant = 0.0
    dominant_emotion = ''
    anger = fr['emotionPredictions'][0]['emotion']['anger']
    if dominant < anger: 
        dominant = anger
        dominant_emotion = 'anger'
    disgust = fr['emotionPredictions'][0]['emotion']['disgust']
    if dominant < disgust: 
        dominant = disgust
        dominant_emotion = 'disgust'
    fear = fr['emotionPredictions'][0]['emotion']['fear']
    if dominant < fear: 
        dominant = fear
        dominant_emotion = 'fear'
    joy = fr['emotionPredictions'][0]['emotion']['joy']
    if dominant < joy: 
        dominant = joy
        dominant_emotion = 'joy'
    sadness = fr['emotionPredictions'][0]['emotion']['sadness']
    if dominant < sadness: 
        dominant = sadness
        dominant_emotion = 'sadness'
    return {'anger': str(anger),
            'disgust': str(disgust),
            'fear': str(fear),
            'joy': str(joy),
            'sadness': str(sadness),
            'dominant_emotion': dominant_emotion}
