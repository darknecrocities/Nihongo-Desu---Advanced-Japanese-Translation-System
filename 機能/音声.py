from gtts import gTTS

def 音声生成(テキスト, 言語):
    音声 = gTTS(text=テキスト, lang=言語)
    ファイル名 = "音声.mp3"
    音声.save(ファイル名)
    return ファイル名
