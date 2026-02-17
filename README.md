# 🚀 Nihongo Desu - Advanced Japanese Translation System

## 概要 / Overview

Nihongo Desu は、英語と日本語間の高度な翻訳を提供する Streamlit ベースのアプリケーションです。言語検出、テキスト翻訳、音声生成、履歴管理などの機能を備えています。

Nihongo Desu is an advanced Japanese translation system built with Streamlit, providing seamless translation between English and Japanese. It features automatic language detection, text translation, audio generation, and history management.

## 🌟 特徴 / Features

- **自動言語検出 / Automatic Language Detection**: 入力テキストの言語を自動的に検出
- **双方向翻訳 / Bidirectional Translation**: 英語 ↔ 日本語の翻訳
- **音声生成 / Audio Generation**: 翻訳結果の音声出力 (gTTS 使用)
- **ファイル翻訳 / File Translation**: テキストファイルのアップロードと翻訳
- **翻訳履歴 / Translation History**: 過去の翻訳を保存・表示
- **ダークテーマ / Dark Theme**: 目に優しいインターフェース
- **ダウンロード機能 / Download Feature**: 翻訳結果のテキストダウンロード

## 📋 要件 / Requirements

- Python 3.8+
- Streamlit
- deep-translator
- gtts
- langdetect
- pandas

## 🛠 インストール / Installation

1. リポジトリをクローン / Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nihongo-desu.git
   cd nihongo-desu
   ```

2. 仮想環境を作成 / Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. 依存関係をインストール / Install dependencies:
   ```bash
   pip install -r 要件.txt
   ```

## 🚀 使用方法 / Usage

1. アプリケーションを起動 / Start the application:
   ```bash
   streamlit run アプリ.py
   ```

2. ブラウザで http://localhost:8501 にアクセス / Open http://localhost:8501 in your browser

3. 翻訳を開始 / Start translating:
   - テキスト入力欄に翻訳したいテキストを入力 / Enter text to translate
   - またはテキストファイルをアップロード / Or upload a text file
   - 「🚀 翻訳開始」ボタンをクリック / Click the "🚀 翻訳開始" button

## 📖 使用例 / Examples

### 基本的な翻訳 / Basic Translation

**英語 → 日本語 / English to Japanese:**
- 入力 / Input: "Hello, how are you?"
- 出力 / Output: "こんにちは、お元気ですか？"

**日本語 → 英語 / Japanese to English:**
- 入力 / Input: "こんにちは"
- 出力 / Output: "Hello"

### ファイル翻訳 / File Translation

1. テキストファイル (.txt) をアップロード / Upload a text file (.txt)
2. 内容が自動的に読み込まれます / Content is automatically loaded
3. 翻訳を実行 / Run translation

## 🏗 アーキテクチャ / Architecture

```
nihongo-desu/
├── アプリ.py                 # メインアプリケーション / Main application
├── 要件.txt                 # 依存関係 / Dependencies
├── 翻訳/                    # 翻訳モジュール / Translation modules
│   ├── 翻訳エンジン.py      # Google Translate API ラッパー / Google Translate wrapper
│   ├── 言語検出.py          # 言語検出機能 / Language detection
│   └── キャッシュ.py        # 翻訳キャッシュ / Translation cache
├── データ/                  # データ管理 / Data management
│   ├── 履歴管理.py          # 翻訳履歴 / Translation history
│   ├── ログ管理.py          # アプリケーションログ / Application logs
│   └── 統計.py              # 使用統計 / Usage statistics
├── 機能/                    # 追加機能 / Additional features
│   ├── 音声.py              # 音声生成 / Audio generation
│   ├── ファイル翻訳.py      # ファイル処理 / File processing
│   └── ダウンロード.py      # ダウンロード機能 / Download feature
├── 設定/                    # 設定 / Settings
│   ├── 設定管理.py          # 言語設定 / Language settings
│   └── テーマ.py            # UIテーマ / UI theme
└── utils/                   # ユーティリティ / Utilities
    └── 日付.py              # 日付処理 / Date utilities
```

## 🔧 設定 / Configuration

### 目標言語の変更 / Change Target Language

`設定/設定管理.py` で目標言語を変更できます / You can change the target language in `設定/設定管理.py`:

```python
def 言語設定():
    return "ja"  # "ja" for Japanese, "en" for English
```

### テーマのカスタマイズ / Theme Customization

`設定/テーマ.py` でダークテーマを有効化 / Enable dark theme in `設定/テーマ.py`

## 📊 統計とログ / Statistics and Logs

- **翻訳回数 / Translation Count**: サイドバーに総翻訳回数を表示 / Total translation count shown in sidebar
- **ログファイル / Log Files**: `データ/アプリログ.log` に詳細なログを記録 / Detailed logs saved to `データ/アプリログ.log`
- **履歴ファイル / History File**: `データ/履歴.json` に翻訳履歴を保存 / Translation history saved to `データ/履歴.json`

## 🐛 トラブルシューティング / Troubleshooting

### 翻訳エラー / Translation Errors
- インターネット接続を確認してください / Check your internet connection
- Google Translate API の制限を確認 / Check Google Translate API limits

### 言語検出の問題 / Language Detection Issues
- 短いテキストの場合は英語と仮定されます / Short texts are assumed to be English
- 特殊文字を含むテキストは正確に検出されない場合があります / Texts with special characters may not be detected accurately

### 音声生成エラー / Audio Generation Errors
- gTTS がインターネットを必要とします / gTTS requires internet connection
- 長いテキストは音声生成に失敗する可能性があります / Long texts may fail audio generation

## 🤝 貢献 / Contributing

1. このリポジトリをフォーク / Fork this repository
2. 機能ブランチを作成 / Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット / Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. ブランチをプッシュ / Push to the branch (`git push origin feature/AmazingFeature`)
5. プルリクエストを作成 / Open a Pull Request

## 📄 ライセンス / License

このプロジェクトは MIT ライセンスの下でライセンスされています / This project is licensed under the MIT License.

## 🙏 謝辞 / Acknowledgments

- [Streamlit](https://streamlit.io/) - UI フレームワーク / UI Framework
- [deep-translator](https://github.com/nidhaloff/deep-translator) - 翻訳ライブラリ / Translation library
- [gTTS](https://github.com/pndurette/gtts) - 音声生成 / Text-to-speech
- [langdetect](https://github.com/Mimino666/langdetect) - 言語検出 / Language detection

## 📞 サポート / Support

質問や問題がある場合は、Issue を開いてください / For questions or issues, please open an Issue.

---

**開発者 / Developer**: Arron Kian Parejas
**バージョン / Version**: 1.0.0
**最終更新 / Last Updated**: 2026
