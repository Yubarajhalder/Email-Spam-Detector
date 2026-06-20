import io
import json
import os
from datetime import datetime

import joblib
from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    session,
    url_for,
)
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "spam-detector-secret-key-2024")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")
METRICS_PATH = os.path.join(BASE_DIR, "model_metrics.json")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

with open(METRICS_PATH, encoding="utf-8") as f:
    METRICS = json.load(f)

LABEL_MAP = {0: "Spam", 1: "Ham"}


def get_probabilities(text):
    """Return prediction label and spam/ham probabilities."""
    features = vectorizer.transform([text])
    prediction = int(model.predict(features)[0])
    proba = model.predict_proba(features)[0]
    spam_prob = round(proba[0] * 100, 2)
    ham_prob = round(proba[1] * 100, 2)
    return prediction, spam_prob, ham_prob


def add_to_history(entry):
    history = session.get("history", [])
    history.insert(0, entry)
    session["history"] = history[:10]
    session.modified = True


@app.route("/")
def index():
    return render_template("index.html", metrics=METRICS, history=session.get("history", []))


@app.route("/about")
def about():
    return render_template("about.html", metrics=METRICS)


@app.route("/predict", methods=["POST"])
def predict():
    email_text = request.form.get("email_text", "").strip()

    if not email_text:
        flash("Please enter an email.", "warning")
        return redirect(url_for("index"))

    prediction, spam_prob, ham_prob = get_probabilities(email_text)
    label = LABEL_MAP[prediction]

    result = {
        "email_text": email_text,
        "prediction": label,
        "spam_prob": spam_prob,
        "ham_prob": ham_prob,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    session["last_result"] = result
    add_to_history(result)
    return render_template("result.html", result=result, metrics=METRICS)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    data = request.get_json(silent=True) or {}
    email_text = (data.get("email_text") or "").strip()

    if not email_text:
        return jsonify({"error": "Please enter an email."}), 400

    prediction, spam_prob, ham_prob = get_probabilities(email_text)
    label = LABEL_MAP[prediction]

    result = {
        "prediction": label,
        "spam_prob": spam_prob,
        "ham_prob": ham_prob,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    add_to_history({**result, "email_text": email_text[:120] + ("..." if len(email_text) > 120 else "")})
    return jsonify(result)


@app.route("/download-report")
def download_report():
    last = session.get("last_result")
    if not last:
        flash("No prediction available for report.", "warning")
        return redirect(url_for("index"))

    email_text = last["email_text"]
    label = last["prediction"]
    spam_prob = last["spam_prob"]
    ham_prob = last["ham_prob"]
    timestamp = last["timestamp"]

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 12, "Email Spam Detection Report", ln=True, align="C")
    pdf.ln(4)

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 8, f"Generated: {timestamp}", ln=True)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Prediction Result", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 8, f"Classification: {label}", ln=True)
    pdf.cell(0, 8, f"Spam Probability: {spam_prob}%", ln=True)
    pdf.cell(0, 8, f"Ham Probability: {ham_prob}%", ln=True)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Email Content", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(0, 6, email_text)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Model Information", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, f"Model: {METRICS['model_type']}", ln=True)
    pdf.cell(0, 6, f"Vectorizer: {METRICS['vectorizer']}", ln=True)
    pdf.cell(0, 6, f"Accuracy: {METRICS['accuracy']}%", ln=True)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="spam_detection_report.pdf",
        mimetype="application/pdf",
    )


@app.route("/clear-history", methods=["POST"])
def clear_history():
    session.pop("history", None)
    flash("Prediction history cleared.", "info")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
