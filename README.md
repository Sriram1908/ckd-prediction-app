# 🩺 CKD Prediction Web App

A simple Flask web application that predicts **Chronic Kidney Disease (CKD)** based on 24 medical input parameters.

---

## 🔍 Project Overview

This project utilizes a trained **SVM (Support Vector Machine)** model to assess the likelihood of CKD. Users provide their medical details through a web form, and the app instantly returns a prediction.

---

## 🛠️ Tech Stack

- 🐍 Python  
- ⚙️ Flask  
- 📊 Scikit-learn  
- 🌐 HTML/CSS  
- 🧪 Jupyter Notebook  
- 🗃️ Git & GitHub  

---

## 📁 Project Structure

CKD_Deployment/
│
├── app.py # Flask backend
├── svm_classifier_pipeline.pkl # Trained ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation
│
├── templates/ # HTML templates (index.html, result.html)
├── static/ # Static assets (CSS, images)
├── ScreenShots/ # Output screenshots
└── CKD_Model_Training.ipynb # Jupyter notebook for model training



---

## 🧪 How to Run the Project Locally

```bash
# 1. Clone the repository
git clone https://github.com/Sriram1908/ckd-prediction-app.git
cd ckd-prediction-app

# 2. Create and activate virtual environment (Windows)
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

➡️ Open http://127.0.0.1:5000 in your browser to use the web app.

📷 Output Screenshots
Screenshots of homepage, input form, and result pages are available in the ScreenShots folder.

🙋‍♂️ Author
Sriram Y
GitHub: Sriram1908
