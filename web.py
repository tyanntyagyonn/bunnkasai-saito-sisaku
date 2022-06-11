import streamlit as st
 
最初 = True

#複数ページの設置

def 初期ページ():
    st.title("科学部　文化祭　特設サイト")
    最初 = False

def 工学班():
   st.title("工学班")
   最初 = False

def 生物班():
   st.title("生物班")
   最初 = False

def 化学班():
   st.title("化学班")
   最初 = False

#サイドバーの設定およびページ移動

st.sidebar.title("目次")

if st.sidebar.button("科学部　文化祭"):
    最初 = True

if st.sidebar.button("科学部　工学班"):
   工学班()

if st.sidebar.button("科学部　生物班"):
   生物班()

if st.sidebar.button("科学部　化学班"):
   化学班()

if 最初 == True:
    初期ページ()