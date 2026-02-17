# 設定/テーマ.py
# Streamlit 用のダークテーマ設定

import streamlit as st

def ダークテーマ():
    """
    ページ全体をダークテーマにする
    """
    st.markdown(
        """
        <style>
        body {
            background-color: #0E1117;
            color: white;
        }
        .stButton>button {
            background-color: #1E1E2E;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
