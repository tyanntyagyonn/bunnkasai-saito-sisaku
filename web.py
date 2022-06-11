import streamlit as st
st.title("科学部")
st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "MObile phone")
)
if st.button("Button1"):
   st.write("Button1 clicked")

if st.button("Button2"):
   st.write("Button2 clicked")