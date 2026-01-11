import streamlit as st

st.title("Chai Taste Poll")

coL1, coL2 = st.columns(2)

with coL1:
    st.header("Masala Chai")
    st.image("https://www.vegrecipesofindia.com/wp-content/uploads/2016/06/masala-chai-recipe.jpg", width=100)
    vote1 = st.button("Vote for Masala Chai")
with coL2:
    st.header("Ginger Chai")
    st.image("https://myfoodstory.com/wp-content/uploads/2020/08/Adrak-Chai-Ginger-Tea-2.jpg", width=200)
    vote2 = st.button("Vote for Ginger Chai") 

if vote1:
    st.success("Thanks for voting Masala Chai!")
elif vote2:
    st.success("Thanks for voting Ginger Chai!")

name = st.sidebar.text_input("Enter your namr")
tea = st.sidebar.selectbox("Choose your chai", ["Masala Chai", "Ginger Chai", "Kashmiri Chai", "Lemon Chai"])               
st.write(f"Welcome {name} and your {tea} is getting ready")
with st.expander("See Chai Preparation Steps"):
    st.write("""
    1. Boil water
    2. Add tea Leaves
    3. Add spices and milk
    4. Add sugar as per taste
    5. Strain and serve hot
    6. Enjoy your chai!         
""")