import streamlit as st

#初期設定

st.session_state.工学班 == False
st.session_state.生物班 == False
st.session_state.化学班 == False

def 工学班():
   st.title("工学班")
def 生物班():
   st.title("工学班")
def 化学班():
   st.title("化学班")

def 工学班ページ():
   if st.session_state.工学班 == True:
      工学班()
def 生物班ページ():
   if st.session_state.工学班 == True:
      生物班()
def 化学班ページ():
   if st.session_state.工学班 == True:
      化学班()

def 班ページ():
   if st.button("工学班 "):
      if st.session_state.工学班 == False:
         st.session_state.工学班 = True
      else:
         st.session_state.工学班 = False
      工学班ページ()
   if st.button("生物班 "):
      if st.session_state.生物班 == False:
         st.session_state.生物班 = True
      else:
         st.session_state.生物班 = False
      生物班ページ()
   if st.button("化学班 "):
      if st.session_state.化学班 == False:
         st.session_state.化学班 = True
      else:
         st.session_state.化学班 = False
      化学班ページ()


#ページ表示
st.title("中等部科学部掲示板")
#班ごとの掲示板表示
班ページ()

