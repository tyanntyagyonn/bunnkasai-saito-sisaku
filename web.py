import streamlit as st
st.title("科学部")
st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "MObile phone")
)