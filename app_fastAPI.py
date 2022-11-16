from joblib import load
import re

from Tools.demo import vector
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from preprocessing_pipeline import preprocess_tweet
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
import pickle


#model = loaded_model = pickle.load(open("trained_lr.0.1.0.pkl", 'rb'))

app = FastAPI(debug=True)



#class get_tweet(BaseModel):
#  def __init__(__pydantic_self__, **data: Any):
#        super().__init__(data)
#        __pydantic_self__.get_tweet = None

#    text: str


@app.get('/')
def home():
    return {'text': "Sentiment Analysis Prediction"}


@app.get('/prediction')
def predict(tw:str):
    text = tw
    preprocess_tw = preprocess_tweet(text)
    model = pickle.load(open("trained_lr.0.1.4.pkl", 'rb'))
    prediction = model.predict([preprocess_tw])
    prediction = int(prediction)
    if prediction > 0:
        prediction = "positive"
    else:
        prediction = "negative"

    return {"sentence": tw, "prediction": prediction}







if __name__ == '__main__':
    uvicorn.run(app)
