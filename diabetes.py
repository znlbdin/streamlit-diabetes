# importing python library
import streamlit as st
import pickle

# loading model
diabetes_model = pickle.load(open("diabetes_model.sav", "rb"))

# judul halaman web
st.title("Data Mining Prediksi Diabetes")

# membagi halaman menjadi 2 kolom
col1, col2 = st.columns(2)

# membuat form imputan
with col1:
    Pregnancies = st.number_input("Input Nilai Pregnancies")

with col2:
    Glucose = st.number_input("Input Nilai Glucose")

with col1:
    BloodPressure = st.number_input("Input Nilai BloodPressure")

with col2:
    SkinThickness = st.number_input("Input Nilai SkinThickness")

with col1:
    Insulin = st.number_input("Input Nilai Insulin")

with col2:
    BMI = st.number_input("Input Nilai BMI")

with col1:
    DiabetesPedigreeFunction = st.number_input(
        "Input Nilai DiabetesPedigreeFunction")

with col2:
    Age = st.number_input("Input Nilai Age")

# code untuk prediksi
diab_diagnosis = ""

# button prediksi
if st.button("Test Diagnosis"):
    diab_prediction = diabetes_model.predict(
        [
            [
                Pregnancies,
                Glucose,
                BloodPressure,
                SkinThickness,
                Insulin,
                BMI,
                DiabetesPedigreeFunction,
                Age,
            ]
        ]
    )

    if diab_prediction[0] == 0:
        diab_diagnosis = "Pasien Tidak Terdiagnosis Diabetes"
    else:
        diab_diagnosis = "Pasien Terdiagnosis Diabetes"

    st.success(diab_diagnosis)
