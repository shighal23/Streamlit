import streamlit as st
from datetime import date

st.title("Welcome to your interactive Age Calculator App")
st.subheader("Calculate your age with Streamlit")
st.text("Enter your date of birth to calculate your age")
dob = st.date_input("Select your date of birth",
                     min_value=date(1900, 1, 1),
                        max_value=date.today())
if dob:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"You are {age} years old.")
    st.success("Age calculation complete!")
    




