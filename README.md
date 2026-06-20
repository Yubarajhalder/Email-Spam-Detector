# AI Email Spam Detector

A modern, responsive Flask web application for detecting email spam using Machine Learning. Built with Python Flask, Scikit-learn, Bootstrap 5, and a trained Logistic Regression classifier.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.6-orange)

## Features

- **Instant Email Classification** — Paste any email and get Spam/Ham prediction in seconds
- **Confidence Scores** — View spam and ham probabilities with animated progress bars
- **Dark Mode** — Toggle between light and dark themes
- **Example Emails** — Load sample spam or ham messages with one click
- **Prediction History** — Session-based history of recent predictions
- **PDF Reports** — Download detailed prediction reports
- **Responsive Design** — Works on desktop, tablet, and mobile
- **Glassmorphism UI** — Modern AI-inspired design with gradient backgrounds

## Project Structure

```
Email-Spam-Detector/
├── app.py                  # Flask application
├── model.pkl               # Trained Logistic Regression model
├── vectorizer.pkl          # TF-IDF vectorizer
├── model_metrics.json      # Model performance metrics
├── train_and_save.py       # Script to retrain and export models
├── requirements.txt        # Python dependencies
├── mail_data.csv           # Training dataset
├── static/
│   ├── css/style.css       # Custom styles
│   ├── js/script.js        # Frontend interactivity
│   └── images/hero.svg     # Hero illustration
└── templates/
    ├── base.html           # Base layout
    ├── index.html          # Home page
    ├── result.html         # Prediction results
    └── about.html          # About page
```

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train Model (if needed)

If `model.pkl` and `vectorizer.pkl` don't exist, run:

```bash
python train_and_save.py
```

### 3. Run the Application

```bash
python app.py
```

Open your browser and navigate to **http://localhost:5000**

## Model Details

| Metric     | Value   |
|------------|---------|
| Algorithm  | Logistic Regression |
| Vectorizer | TF-IDF (7,440 features) |
| Accuracy   | ~96.77% |
| Precision  | ~96.41% |
| Recall     | ~100%   |
| F1 Score   | ~98.17% |
| Dataset    | SMS Spam Collection |

**Label Encoding:** `0` = Spam, `1` = Ham

## API Endpoint

```
POST /api/predict
Content-Type: application/json

{
  "email_text": "Your email content here"
}
```

**Response:**

```json
{
  "prediction": "Spam",
  "spam_prob": 98.5,
  "ham_prob": 1.5,
  "timestamp": "2024-01-15 14:30:00"
}
```

## Routes

| Route              | Method | Description                |
|--------------------|--------|----------------------------|
| `/`                | GET    | Home page with analyzer    |
| `/about`           | GET    | About the project          |
| `/predict`         | POST   | Submit email for prediction|
| `/api/predict`     | POST   | JSON API for predictions   |
| `/download-report` | GET    | Download PDF report        |
| `/clear-history`   | POST   | Clear session history      |

## Tech Stack

- **Backend:** Python Flask
- **ML:** Scikit-learn (Logistic Regression + TF-IDF)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Icons:** Font Awesome 6
- **Font:** Inter (Google Fonts)
- **PDF:** fpdf2

## License

MIT License — feel free to use this project for learning and development.
