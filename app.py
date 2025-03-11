import streamlit as st
import pickle
import pandas as pd
import os

# Correct file path based on your GitHub structure
model_path = os.path.join(os.getcwd(), 'your_model.pkl')

# Check if the model file exists
if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    st.error("Model file not found. Please ensure 'your_model.pkl' is uploaded to your repository.")

# Streamlit UI
st.title("Waiter Tips Prediction Model")
st.write("This app predicts waiter tips based on total bill and group size.")

# Input fields for user data
total_bill = st.number_input("Enter Total Bill Amount ($)")
size = st.number_input("Enter Size of Dining Group")

# Prediction button
if st.button("Predict Tip"):
    if total_bill > 0 and size > 0:
        prediction = model.predict([[total_bill, size]])
        st.success(f"Predicted Tip Amount: ${prediction[0]:.2f}")
    else:
        st.warning("Please enter valid input values.")
