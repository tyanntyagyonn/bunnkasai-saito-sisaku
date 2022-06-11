import streamlit as st

if 'pezibangou' not in st.session_state:
  st.session_state.pezibangou = 0



#ボタン設定

def ボタン():
   if st.button("中等部科学部"):
      st.session_state.pezibangou = 0

   if st.button("中等部科学部"):
      st.session_state.pezibangou = 1

   if st.button("中等部科学部"):
      st.session_state.pezibangou = 2

   if st.button("中等部科学部"):
      st.session_state.pezibangou = 3
      


#ページごとのプログラム

def 初期ページ():
   st.title("中等部科学部")
   ボタン()

def 工学班():
   st.title("工学班")
   ボタン()

def 生物班():
   st.title("生物班")
   ボタン()

def 化学班():
   st.title("化学班")
   ボタン()



#ページ番号変更

st.sidebar.title("目次")

if st.sidebar.button("中等部科学部"):
   st.session_state.pezibangou = 0

if st.sidebar.button("科学部　工学班"):
   st.session_state.pezibangou = 1

if st.sidebar.button("科学部　生物班"):
   st.session_state.pezibangou = 2

if st.sidebar.button("科学部　化学班"):
   st.session_state.pezibangou = 3



#ページ移動

if st.session_state.pezibangou == 0:
   初期ページ()
elif st.session_state.pezibangou == 1:
   工学班()
elif st.session_state.pezibangou == 2:
   生物班()
else:
   化学班()