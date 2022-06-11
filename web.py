import streamlit as st
#ワイド表示
st.set_page_config(layout="wide")
#セレクトボックスのリストを作成
pagelist = ["page1","page2"]
#サイドバーのセレクトボックスを配置
selector=st.sidebar.selectbox( "ページ選択",pagelist)
if selector=="page1":
    if st.button('ページ1ボタン'):
        st.title("ページ1のタイトル")
elif selector=="page2":
    if st.button('ページ2ボタン'):
        st.title("ページ2のタイトル")