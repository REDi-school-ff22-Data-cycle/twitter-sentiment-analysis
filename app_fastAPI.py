import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
import uvicorn
import pickle


app = FastAPI(debug= True)


# https://www.youtube.com/watch?v=0s-oat69UqU&t=2s&ab_channel=MicrosoftPowerTools

@app.get('/')
def home():
    return {'message': "Charles & Lucia's first FastAPI ML "}

@app.get('/predict')
def predict(Message: str):
    text = [Message]
    model= pickle.load(open("trained_lr.0.1.0.3.pkl", 'rb'))
    makeprediction = model.predict([Message])
    output = makeprediction

    return f" First try {output}"


# Ideas from: https://github.com/Jitendra-Dash/Sentiment-classification-deployement-of-ML-model-using-FastAPI/blob/main/main.py#L7
# https://www.youtube.com/watch?v=k_ngUNieJyg&ab_channel=JitendraDash

class get_review(BaseModel):
    review :str

@app.post("/prediction")
def get_prediction(gr:get_review):
    text = [gr.review]
    vec = vector.transform(text)
    prediction = model.predict(vec)
    prediction = int(prediction)
#    if prediction >0:  check for our output
#        prediction="positive"
#    else:
#        prediction = "negative"
#
#    return {"sentence":gr.review,"prediction":prediction}




if __name__ == '__main__':
    uvicorn.run(app)
