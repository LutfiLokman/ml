import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

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


bow_transformer = CountVectorizer().fit(df["text"])
bow = bow_transformer.transform(df["text"])
bow_matrix = pd.DataFrame(
    bow.toarray(), columns=bow_transformer.get_feature_names_out()
)

tfidf_transformer = TfidfTransformer().fit(bow)
X = tfidf_transformer.transform(bow)
tfidf_matrix = pd.DataFrame(
    X.toarray(), columns=bow_transformer.get_feature_names_out()
)

y = df["label"]

model = MultinomialNB()

model.fit(X, y)

X_test = tfidf_transformer.transform(
    bow_transformer.transform(["maserati jaguar mercedes proton"])
)

model.predict(X_test)

results = pd.DataFrame(model.predict_proba(X_test), columns=model.classes_)
