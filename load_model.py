from preprocessing_pipeline import preprocess_data
import pickle


def load_model(text):
    text = preprocess_data(text)
    loaded_model = pickle.load(open("trained_lr.0.1.0.pkl", 'rb'))
    # result = loaded_model.score(X_test, Y_test)
    print(loaded_model)



