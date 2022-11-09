import pickle
import sklearn


def load_model():
    loaded_model = pickle.load(open("trained_lr.0.1.0.pkl", 'rb'))
    #result = loaded_model.score(X_test, Y_test)
    print(loaded_model)




#Logistic Regression Pipeline
lr = Pipeline([('tfidf',TfidfVectorizer()),
              ('clf',LogisticRegression(C=1,
                                         class_weight='balanced',
                                         max_iter=1000))])



# Split 3
# Random split train and test data.
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix,classification_report
# Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle

X_train, X_test, y_train, y_test = train_test_split(df_upsampled_n_p['message'], df_upsampled_n_p['sentiment'], test_size=0.33, random_state=42)

# count vectorizer 3:

#vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
#train_matrix = vectorizer.fit_transform(X_train)
#test_matrix = vectorizer.transform(X_test)

# Logistic Regression
#from sklearn.linear_model import LogisticRegression
#lr = LogisticRegression(max_iter=500) # Here we increased the max_iter to converge.


lr = Pipeline([('tfidf',TfidfVectorizer()),
              ('clf',LogisticRegression(C=1,
                                         class_weight='balanced',
                                         max_iter=500))])
# Fit


X_train, X_test, y_train, y_test = train_test_split(df_upsampled_n_p['message'], df_upsampled_n_p['sentiment'], test_size=0.33, random_state=42)

# Fit
lr.fit(X_train, y_train)

# Prediction
predictions = lr.predict(X_test)

# To test the accuracy of the model:
# find accuracy, precision, recall:

new = np.asarray(y_test)
confusion_matrix(predictions,y_test)

# The results should be a confusion matrix

print(classification_report(predictions,y_test))
