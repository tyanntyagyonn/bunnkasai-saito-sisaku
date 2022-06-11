import streamlit as st
# タイトル
st.title('科学部')
# ヘッダ
st.header('科学部')
# 純粋なテキスト
st.text('科学部')
# サブレベルヘッダ
st.subheader('科学部')
# マークダウンテキスト
st.markdown('科学部')
# LaTeX テキスト
st.latex(r'\bar{X} = \frac{1}{N} \sum_{n=1}^{N} x_i')
# コードスニペット
st.code('科学部')
# エラーメッセージ
st.error('科学部')
# 警告メッセージ
st.warning('科学部')
# 情報メッセージ
st.info('科学部')
# 成功メッセージ
st.success('科学部')
# 例外の出力
st.exception(Exception('科学部'))