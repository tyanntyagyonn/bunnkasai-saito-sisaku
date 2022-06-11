import streamlit as st
st.title("科学部")
st.sidebar.title("目次")
st.sidebar.button("科学部　文化祭")
st.button("科学部工学班")
st.sidebar.button("科学部　化学班")
st.sidebar.button("科学部　生物班")

def page1():
   st.write("Here is page 1.")

def page2():
   st.write("Here is page 2.")

if st.sidebar.button("Button1"):
   page1()

if st.sidebar.button("Button2"):
   page2()