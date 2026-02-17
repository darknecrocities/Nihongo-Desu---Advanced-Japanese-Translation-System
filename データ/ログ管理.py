# データ/ログ管理.py
# アプリケーションログ管理モジュール

import os
import logging

ログフォルダ = "データ"
ログファイル = os.path.join(ログフォルダ, "アプリログ.log")

# フォルダが存在しない場合は作成
if not os.path.exists(ログフォルダ):
    os.makedirs(ログフォルダ)

# ロガー設定
logging.basicConfig(
    filename=ログファイル,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def 情報ログ(メッセージ):
    """
    通常情報ログを記録
    """
    logging.info(メッセージ)

def エラーログ(メッセージ):
    """
    エラーログを記録
    """
    logging.error(メッセージ)

def 警告ログ(メッセージ):
    """
    警告ログを記録
    """
    logging.warning(メッセージ)
