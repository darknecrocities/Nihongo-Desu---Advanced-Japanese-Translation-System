from langdetect import detect

def 言語を検出する(文章):
    """
    文章の言語を ISO 639-1 コードで返す
    """
    try:
        detected = detect(文章)
        # For short texts, langdetect can be unreliable; if not English or Japanese, assume English
        if detected not in ["en", "ja"]:
            return "en"
        return detected
    except:
        # 検出できなかった場合は英語と仮定
        return "en"
