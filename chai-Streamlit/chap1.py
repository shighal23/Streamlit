import streamlit as st

st.title("Welcome to Chai Streamlit App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your fav. variety of chai")

chai = st.selectbox("Your fav. chai: ", 
                    ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Tulsi Chai", "Lemon Chai"])
st.write(f"Your choose {chai}. Excellent choise")

st.success("Your chai has been brewed")