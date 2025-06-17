from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib  # or use pickle

app = Flask(__name__)
model = joblib.load('svm_classifier_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Collect inputs in the same order as training
            data = [
                float(request.form['age']),
                float(request.form['bp']),
                float(request.form['sg']),
                float(request.form['al']),
                float(request.form['su']),
                int(request.form['rbc']),
                int(request.form['pc']),
                int(request.form['pcc']),
                int(request.form['ba']),
                float(request.form['bgr']),
                float(request.form['bu']),
                float(request.form['sc']),
                float(request.form['sod']),
                float(request.form['pot']),
                float(request.form['hemo']),
                float(request.form['pcv']),
                float(request.form['wc']),
                float(request.form['rc']),
                int(request.form['htn']),
                int(request.form['dm']),
                int(request.form['cad']),
                int(request.form['appet']),
                int(request.form['pe']),
                int(request.form['ane'])
            ]

            # Column names matching the training dataset
            columns = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr',
                       'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wc', 'rc',
                       'htn', 'dm', 'cad', 'appet', 'pe', 'ane']

            # Create DataFrame
            df_input = pd.DataFrame([data], columns=columns)

            # DEBUG: Print the final input to the model
            print("✅ FINAL INPUT TO MODEL:")
            print(df_input)

            # Get prediction and probability
            prediction = model.predict(df_input)[0]

            # If your model supports predict_proba, print probabilities
            if hasattr(model, 'predict_proba'):
                proba = model.predict_proba(df_input)[0]
                print(f"🔍 Prediction: {prediction}, Probabilities: {proba}")
            else:
                print(f"🔍 Prediction: {prediction}")

            return render_template('result.html', prediction=prediction)

        except Exception as e:
            return f"❌ Error occurred: {str(e)}"

@app.route('/form')
def show_form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
