import streamlit as st
from datetime import date

st.title("Chai Maker App")

if st.button("Make Chai"):
    st.success("Chai is being brewed! Enjoy your cup of chai.")

add_masala = st.checkbox("Add Masala")   

if add_masala:
    st.write("Masala added to your chai!")

tea_type = st.radio("Pick your chai base: ",
                    ["Milk", "Water", "Almond Milk"])
st.write(f"Selected base {tea_type}") 
flavour = st.selectbox("Choose flavour: ",
                          ["Adrak", "Kesar", "Tulsi"])  
st.write(f"Selected Flavour {flavour}") 

sugar = st.slider("Sugar level (spoon)", 0, 5, 2) 
st.write(f"Selected sugar level {sugar}")

cups = st.number_input("How many cups", min_value=1,
                       max_value=10, step=1)
st.write(f"Selected sugar level {cups}")

name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name} ! Your chai is on the way")

dob = st.date_input("Select your date of birth",
                     min_value=date(1900, 1, 1),
                        max_value=date.today())
today = date.today()
age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
st.write(f"You are {age} years old.")
st.success("Your date of birth recorded.")
