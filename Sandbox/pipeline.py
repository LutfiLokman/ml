import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
df = pd.DataFrame(
    {
        "text": [
            "cat cow jaguar",
            "ferrari jaguar maserati",
            "mercedes ferrari jaguar ferrari",
            "cow elephant cow cat",
            "ferrari jaguar maserati mercedes",
        ],
        "label": ["animal", "car", "car", "animal", "car"],
    }
)

pipe_nb = Pipeline([("tfidf", TfidfVectorizer()), ("classifier", MultinomialNB())])

pipe_nb.fit(df["text"], df["label"])

pipe_log = Pipeline([("tfidf", TfidfVectorizer()), ("classifier", SGDClassifier(loss='log'))])

pipe_log.fit(df["text"], df["label"])

X_test = ['mercedes jaguar maserati']

pipe_nb.predict(X_test)

pipe_nb.predict_proba(X_test)

pipe_log.predict(X_test)

pipe_log.predict_proba(X_test)
