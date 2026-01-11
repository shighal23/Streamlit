import streamlit as st

st.title("Chai Taste Poll")

col1, col2 = st.columns(2)

with col1:
    st.header("Masala chai")
    st.image("https://shivanilovesfood.com/wp-content/uploads/2022/08/Chai-6.jpg", width=100)
    vote1 = st.button("Vote for Masala Chai")

with col2:
    st.header("Ginger chai")
    st.image("https://myfoodstory.com/wp-content/uploads/2020/08/Adrak-Chai-Ginger-Tea-2.jpg", width=200)
    vote2 = st.button("Vote for Ginger Chai")

if vote1:
    st.success("Thanks for voting Masala Chai!")
elif vote2:
    st.success("Thanks for voting Ginger Chai!")

name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("Choose your chai", ["Masala Chai", "Ginger Chai", "Kashmiri Chai", "Lemon Tead"])

st.write(f"Welcome {name} and your {tea} chai is getting ready")


with st.expander("See Chai Preparation Steps"):
    st.write("""
    1. Boil water
    2. Add tea Leaves
    3. Add spices and milk
    4. Add sugar as per taste
    5. Strain and serve hot
    6. Enjoy your chai!
""")

st.markdown('## Welcome to Chai App')
st.markdown('> Blockqoute ')
