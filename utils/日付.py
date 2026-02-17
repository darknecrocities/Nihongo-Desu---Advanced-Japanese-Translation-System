from datetime import datetime

def 現在時刻():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
