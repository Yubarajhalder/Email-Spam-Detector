# 📧 AI Email Spam Detector

🚀 **Live Demo:** https://email-spam-detector-3-nse1.onrender.com

A modern, responsive **Flask web application** that detects whether an email is **Spam** or **Ham** using **Machine Learning**. The project uses **TF-IDF Vectorization** and a **Logistic Regression** classifier trained on the SMS Spam Collection dataset.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6-orange)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

---

## 🌐 Live Demo

👉 https://email-spam-detector-3-nse1.onrender.com

---

## ✨ Features

* 📩 Instant Spam/Ham Prediction
* 📊 Confidence Scores with Probability Bars
* 🌙 Dark & Light Mode
* 📄 Download Prediction Reports as PDF
* 🕒 Prediction History
* 💡 Sample Spam & Ham Emails
* 📱 Fully Responsive Design
* 🎨 Modern Glassmorphism User Interface
* ⚡ REST API for Predictions

---

## 🧠 Machine Learning Pipeline

```
Email Text
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Logistic Regression Model
     │
     ▼
Spam / Ham Prediction
```

---

## 📂 Project Structure

```
Email-Spam-Detector/
│
├── app.py
├── train_and_save.py
├── model.pkl
├── vectorizer.pkl
├── model_metrics.json
├── requirements.txt
├── runtime.txt
├── Procfile
├── mail_data.csv
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/
    ├── base.html
    ├── index.html
    ├── result.html
    └── about.html
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Yubarajhalder/Email-Spam-Detector.git

cd Email-Spam-Detector
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the Model (Optional)

If the trained model files are missing:

```bash
python train_and_save.py
```

### 4. Run the Flask App

```bash
python app.py
```

Open your browser and visit

```
http://localhost:5000
```

---

## 📊 Model Performance

| Metric     | Score               |
| ---------- | ------------------- |
| Algorithm  | Logistic Regression |
| Vectorizer | TF-IDF              |
| Accuracy   | **96.77%**          |
| Precision  | **96.41%**          |
| Recall     | **100%**            |
| F1 Score   | **98.17%**          |
| Dataset    | SMS Spam Collection |

### Label Encoding

```
0 → Spam
1 → Ham
```

---

## 🔌 REST API

### Endpoint

```
POST /api/predict
```

### Request

```json
{
  "email_text": "Congratulations! You won a free iPhone."
}
```

### Response

```json
{
  "prediction": "Spam",
  "spam_prob": 98.5,
  "ham_prob": 1.5,
  "timestamp": "2026-06-21 12:30:00"
}
```

---

## 📍 Available Routes

| Route              | Method | Description         |
| ------------------ | ------ | ------------------- |
| `/`                | GET    | Home Page           |
| `/about`           | GET    | About Project       |
| `/predict`         | POST   | Predict Email       |
| `/api/predict`     | POST   | JSON API            |
| `/download-report` | GET    | Download PDF Report |
| `/clear-history`   | POST   | Clear History       |

---

## 🛠 Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Logistic Regression
* TF-IDF Vectorizer

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Other Libraries

* FPDF2
* Font Awesome
* Google Fonts

---

## 💼 Skills Demonstrated

* Machine Learning
* Natural Language Processing (NLP)
* Text Classification
* Flask Development
* REST API Development
* Model Deployment
* Responsive Web Design
* PDF Generation
* Session Management

---

## 🚀 Future Improvements

* Gmail Integration
* Deep Learning Models (LSTM/BERT)
* Multi-language Spam Detection
* User Authentication
* Database Support
* Email Attachment Analysis

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Yubaraj Halder**

⭐ If you found this project useful, consider giving it a star on GitHub!
