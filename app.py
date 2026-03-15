import streamlit as st
import pickle 
import numpy as np

#load trained data
model = pickle.load(open("model.pkl", "rb"))
st.title("Placement Predictor")
st.write("Enter Student Details")

cgpa = st.number_input("CGPA", min_value = 0.0, max_value = 10.0)
iq = st.number_input("IQ")

if st.button("predict"):
    data = np.array([[cgpa, iq]])
    prediction = model.predict(data)

    if prediction == 1:
        st.success("Passed & Got Placement in Good company")
    else: 
        st.error("Failed, no placement!!! ")