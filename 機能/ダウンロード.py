import streamlit as st

def ダウンロードボタン(内容):
    st.download_button(
        label="翻訳をダウンロード",
        data=内容,
        file_name="translation.txt"
    )
