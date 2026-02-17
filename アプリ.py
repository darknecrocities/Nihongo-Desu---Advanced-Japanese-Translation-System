import streamlit as st
from 翻訳.翻訳エンジン import 翻訳する
from 翻訳.言語検出 import 言語を検出する
from 翻訳.キャッシュ import キャッシュ翻訳
from データ.履歴管理 import 履歴を保存する
from データ.統計 import 翻訳回数
from データ.ログ管理 import 情報ログ, エラーログ
from 機能.音声 import 音声生成
from 機能.ファイル翻訳 import ファイル内容取得
from 機能.ダウンロード import ダウンロードボタン
from 設定.テーマ import ダークテーマ
from 設定.設定管理 import 言語設定
from utils.日付 import 現在時刻
import json
import os

# =============================
# 初期設定
# =============================
st.set_page_config(page_title="日本語翻訳アプリ", layout="wide")
ダークテーマ()

if "翻訳結果" not in st.session_state:
    st.session_state.翻訳結果 = ""

st.title("🚀 高度日本語翻訳システム")
st.markdown("---")

# =============================
# サイドバー
# =============================
st.sidebar.header("⚙ 設定")
目標言語 = st.sidebar.selectbox(
    "目標言語を選択",
    options=["ja", "en"],
    format_func=lambda x: "日本語" if x == "ja" else "英語",
    index=0  # Default to Japanese
)
st.sidebar.write("📊 総翻訳回数:", 翻訳回数())

# =============================
# メインUI
# =============================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 入力")
    文章 = st.text_area("翻訳テキストを入力してください", height=200)
    アップロード = st.file_uploader("テキストファイルアップロード", type=["txt"])

    if アップロード:
        try:
            文章 = ファイル内容取得(アップロード)
            st.success("ファイル読み込み成功")
            情報ログ("ファイルアップロード成功")
        except Exception as e:
            st.error("ファイル読み込みエラー")
            エラーログ(f"ファイル読み込み失敗: {str(e)}")

    翻訳ボタン = st.button("🚀 翻訳開始")

with col2:
    st.subheader("🌍 翻訳結果")
    if st.session_state.翻訳結果:
        st.success("翻訳完了")
        st.write(st.session_state.翻訳結果)
        ダウンロードボタン(st.session_state.翻訳結果)

        try:
            音声ファイル = 音声生成(st.session_state.翻訳結果, 目標言語)
            st.audio(音声ファイル)
        except Exception as e:
            エラーログ(f"音声生成エラー: {str(e)}")

# =============================
# 翻訳処理
# =============================
if 翻訳ボタン:
    if not 文章:
        st.warning("⚠ テキストを入力してください")
    else:
        try:
            with st.spinner("翻訳中..."):
                情報ログ("翻訳開始")

                # 言語検出
                検出言語 = 言語を検出する(文章)
                st.write(f"検出言語: {検出言語}")  # デバッグ表示

                # 翻訳（キャッシュ付き）
                結果 = キャッシュ翻訳(
                    翻訳する,
                    文章,
                    検出言語,
                    目標言語
                )

                if "翻訳エラー" in 結果:
                    st.error(結果)
                    エラーログ(f"翻訳エラー: {結果}")
                else:
                    st.session_state.翻訳結果 = 結果

                    # 履歴保存
                    履歴を保存する({
                        "時間": 現在時刻(),
                        "元言語": 検出言語,
                        "目標言語": 目標言語,
                        "入力": 文章,
                        "出力": 結果
                    })

                    情報ログ("翻訳成功")

                    st.rerun()

        except Exception as e:
            st.error("翻訳中にエラーが発生しました")
            エラーログ(f"翻訳エラー: {str(e)}")

# =============================
# 翻訳履歴表示
# =============================
st.markdown("---")
st.subheader("📜 翻訳履歴")

履歴ファイル = "データ/履歴.json"

if os.path.exists(履歴ファイル):
    try:
        with open(履歴ファイル, "r", encoding="utf-8") as f:
            履歴データ = json.load(f)

        if len(履歴データ) == 0:
            st.info("まだ翻訳履歴はありません")
        else:
            # 最新5件表示
            for item in reversed(履歴データ[-5:]):
                with st.expander(f"{item['時間']} ({item['元言語']} → {item['目標言語']})"):
                    st.write("入力:", item["入力"])
                    st.write("出力:", item["出力"])

    except Exception as e:
        エラーログ(f"履歴表示エラー: {str(e)}")
        st.error("履歴の読み込みに失敗しました")
else:
    st.info("まだ翻訳履歴はありません")
