import streamlit as st
st.title("科学部")
st.sidebar.title("目次")
st.sidebar.button("科学部　文化祭")
st.sidebar.button("科学部　工学班")
st.sidebar.button("科学部　化学班")
st.sidebar.button("科学部　生物班")

def 工学班():
    st.title("工学班")

def 化学班():
    st.title("化学班")

def 生物班():
    st.title("生物班")

if st.button("科学部　工学班"):
    st.title("工学班")