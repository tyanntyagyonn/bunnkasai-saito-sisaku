import streamlit as st



#初期設定

if 'pezibangou' not in st.session_state:

   st.session_state.pezibangou = 0

def 初期ページ():
   st.title("中等部科学部")
def 工学班():
   st.title("工学班")
def 生物班():
   st.title("生物班")
def 化学班():
   st.title("化学班")

def ボタン():
   
   if st.button("中等部科学部掲示板 "):
      st.session_state.pezibangou = 0
   if st.button("科学部工学班掲示板 "):
      st.session_state.pezibangou = 1
   if st.button("科学部生物班掲示板 "):
      st.session_state.pezibangou = 2
   if st.button("科学部化学班掲示板 "):
      st.session_state.pezibangou = 3


"""def サイドバーボタン():

   st.sidebar.title("目次")
   
   if st.sidebar.button("中等部科学部掲示板"):
      st.session_state.pezibangou = 0
      ページ移動()
   if st.sidebar.button("科学部工学班掲示板"):
      st.session_state.pezibangou = 1
      ページ移動()
   if st.sidebar.button("科学部生物班掲示板"):
      st.session_state.pezibangou = 2
      ページ移動()
   if st.sidebar.button("科学部化学班掲示板"):
      st.session_state.pezibangou = 3
      ページ移動()"""

def ページ移動():

   if st.session_state.pezibangou == 0:
      初期ページ()
   elif st.session_state.pezibangou == 1:
      工学班()
   elif st.session_state.pezibangou == 2:
      生物班()
   else:
      化学班()

   ボタン()



ページ移動()
