🧬 Diabetes Prediction Web App

A Streamlit-powered machine learning app to predict whether a person is likely to have diabetes based on key medical parameters.

📊 Project Overview

This interactive web application collects user input (name, age, gender, medical indicators) and uses a trained machine learning model (pickle file) to predict diabetes status in real-time.

📥 User Inputs

🧾 The user provides the following details through a clean form:

🔹 Name (Text Input)

🔹 Gender (Dropdown): Female, Male, Other

🔹 Age (Dropdown from 0 to 120)

🔹 Hypertension (Number Input: 0 or 1)

🔹 Heart Disease (Number Input: 0 or 1)

🔹 Smoking History (Dropdown): never, No info, Current, former, ever, not current

🔹 BMI (Body Mass Index) (Float Input)

🔹 HbA1c Level (Float Input)

🔹 Blood Glucose Level (Float Input)

⚙️ Model Prediction

The model returns either:

1 – indicating the user has diabetes

0 – indicating the user does not have diabetes

✅ A popup shows the result:

"Yuvan, you have diabetes" or
"Yuvan, you do not have diabetes"

🧠 Feature Encoding

Gender:

Female → 0, Male → 1, Other → 2

Smoking History:

never → 0, No info → 1, Current → 2, former → 3, ever → 4, not current → 5

📂 Project Structure

📁 diabetes_app/

├── diabetes.pkl               ← Trained machine learning model

├── diabetes_app.py           ← Streamlit frontend

├── requirements.txt


💡 Technologies Used

Python 3.8 / 3.12

Streamlit

pandas, numpy

scikit-learn (for model training)

Pickle (model serialization)

🏁 Conclusion

This project demonstrates how machine learning and web development can come together to provide real-time health diagnostics in a user-friendly format.
