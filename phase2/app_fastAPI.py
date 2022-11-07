import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_root():
    return {'message': "Charles & Lucia's first FastAPI ML "}
