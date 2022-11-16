import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report
# Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle
# Logistic Regression Pipeline


lr = Pipeline([('tfidf', TfidfVectorizer()),
               ('clf', LogisticRegression(C=1,
                                          class_weight='balanced',
                                          max_iter=500))])
# Fit


X_train, X_test, y_train, y_test = train_test_split(df_upsampled_n_p['message'], df_upsampled_n_p['sentiment'],
                                                    test_size=0.33, random_state=42)

# Fit
lr.fit(X_train, y_train)

# Prediction
predictions = lr.predict(X_test)

# To test the accuracy of the model:
# find accuracy, precision, recall:

new = np.asarray(y_test)
confusion_matrix(predictions, y_test)

# The results should be a confusion matrix

print(classification_report(predictions, y_test))