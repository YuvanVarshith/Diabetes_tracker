import streamlit as st
import numpy as np
import pickle

# Load your trained model
with open("Diabetes.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🩺 Diabetes Prediction Form")

# --- Input Fields ---
name = st.text_input("Name")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])
    age = st.selectbox("Age", list(range(1, 121)))
    hypertension = st.number_input("Hypertension (0 = No, 1 = Yes)", min_value=0, max_value=1, step=1)
    heart_disease = st.number_input("Heart Disease (0 = No, 1 = Yes)", min_value=0, max_value=1, step=1)

with col2:
    smoking_history = st.selectbox("Smoking History", ["never", "No Info", "Current", "former", "ever", "not current"])
    bmi = st.number_input("BMI")
    hba1c_level = st.number_input("HbA1c Level")
    blood_glucose_level = st.number_input("Blood Glucose Level")

# --- Submit Button ---
if st.button("Submit"):
    # Encode gender and smoking history
    gender_map = {"Female": 0, "Male": 1, "Other": 2}
    smoking_map = {
        "never": 0,
        "No Info": 1,
        "Current": 2,
        "former": 3,
        "ever": 4,
        "not current": 5
    }

    gender_val = gender_map.get(gender, -1)
    smoking_val = smoking_map.get(smoking_history, -1)

    # Prepare data for prediction
    input_data = np.array([[
        gender_val, age, hypertension, heart_disease,
        smoking_val, bmi, hba1c_level, blood_glucose_level
    ]])


    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result as popup
    if prediction == 1:
        st.error(f"🔴 {name}, you **have diabetes**.")
    else:
        st.success(f"🟢 {name}, you **do not have diabetes**.")
