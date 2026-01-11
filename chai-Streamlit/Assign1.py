import streamlit as st

st.title("Welcome to Programming language with Streamlit App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your second interactive app")
st.write("Choose your fav. programming Language")
Language = st.selectbox("Your fav. programming Language: ",
                        ["Python", "JavaSrcipt", "Java", "C++", "Go", "Ruby"])
st.write(f"You choose {Language}. Excellent choice")
st.success("You have chosen well!")