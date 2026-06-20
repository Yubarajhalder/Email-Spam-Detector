"""Train spam detection model and export artifacts for Flask app."""
import json

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split

df = pd.read_csv("mail_data.csv")
df.loc[df["Category"] == "spam", "Category"] = 0
df.loc[df["Category"] == "ham", "Category"] = 1

x = df["Message"]
y = df["Category"].astype(int)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(min_df=1, stop_words="english", lowercase=True)
x_train_fe = vectorizer.fit_transform(x_train)
x_test_fe = vectorizer.transform(x_test)

model = LogisticRegression(max_iter=1000)
model.fit(x_train_fe, y_train)

y_pred = model.predict(x_test_fe)

metrics = {
    "accuracy": round(accuracy_score(y_test, y_pred) * 100, 2),
    "precision": round(precision_score(y_test, y_pred) * 100, 2),
    "recall": round(recall_score(y_test, y_pred) * 100, 2),
    "f1_score": round(f1_score(y_test, y_pred) * 100, 2),
    "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
    "model_type": "Logistic Regression",
    "vectorizer": "TF-IDF",
    "dataset": "SMS Spam Collection (mail_data.csv)",
    "features": int(x_train_fe.shape[1]),
    "training_samples": len(x_train),
    "test_samples": len(x_test),
}

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

with open("model_metrics.json", "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

print(json.dumps(metrics, indent=2))
