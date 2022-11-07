import pickle
import sklearn


def load_model():
    loaded_model = pickle.load(open("trained_lr.0.1.0.pkl", 'rb'))
    #result = loaded_model.score(X_test, Y_test)
    print(loaded_model)
