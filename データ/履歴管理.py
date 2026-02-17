import json
import os

履歴ファイル = "データ/履歴.json"

def 履歴を保存する(データ):
    if not os.path.exists(履歴ファイル):
        with open(履歴ファイル, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(履歴ファイル, "r+", encoding="utf-8") as f:
        内容 = json.load(f)
        内容.append(データ)
        f.seek(0)
        json.dump(内容, f, ensure_ascii=False, indent=2)
