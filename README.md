# CKD Prediction Web App

A simple Flask web application that predicts Chronic Kidney Disease (CKD) based on 24 user-input medical parameters.

## 🔍 Project Overview
This project uses a trained SVM classifier to detect the likelihood of CKD. Users input their medical data, and the app predicts the result.

## 🛠️ Tech Stack
- Python
- Flask
- Scikit-learn
- HTML/CSS
- Git/GitHub

## 📁 Project Structure
app.py
templates/
static/
svm_classifier_pipeline.pkl
requirements.txt
ScreenShots/
README.md


## 📷 Output Screenshots
Screenshots of homepage, prediction inputs, and result page are available in the [ScreenShots](./ScreenShots) folder.

## 🧪 How to Run
1. Clone this repo
2. Create virtual environment  
   `python -m venv venv`
3. Activate it  
   `.\venv\Scripts\activate`
4. Install packages  
   `pip install -r requirements.txt`
5. Run the app  
   `python app.py`

## 📚 Dataset
Used the CKD dataset from Kaggle or UCI Repository.

## 🙋 Author
Sriram Y — [GitHub](https://github.com/Sriram1908)
