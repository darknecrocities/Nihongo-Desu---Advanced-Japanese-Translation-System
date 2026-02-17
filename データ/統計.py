import json

def 翻訳回数():
    try:
        with open("データ/履歴.json", "r", encoding="utf-8") as f:
            内容 = json.load(f)
            return len(内容)
    except:
        return 0
