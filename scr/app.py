import streamlit as st
import pandas as pd
import pickle

#correct the path to the model
model_path = 'src/your_model.pkl'

# Load the model
model_path = '/.src/your_model.pkl'
model = pickle.load(open(model_path, 'rb'))

# Streamlit UI
st.title("Waiter Tips Prediction Model")
total_bill = st.number_input("Enter Total Bill Amount ($)")
size = st.number_input("Enter Size of Dining Group", min_value=1, step=1)

# Prediction button
if st.button("Predict Tip"):
    prediction = model.predict([[total_bill, size]])
    st.success(f"Predicted Tip Amount: ${round(prediction[0], 2)}")
