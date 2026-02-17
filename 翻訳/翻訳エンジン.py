from deep_translator import GoogleTranslator

def 翻訳する(文章, 元言語="auto", 目標言語="ja"):
    """
    翻訳関数
    """
    try:
        # deep-translator may fail if target language is invalid
        return GoogleTranslator(source=元言語, target=目標言語).translate(文章)
    except Exception as e:
        # Return the error message for debugging
        return f"翻訳エラー: {str(e)}"
