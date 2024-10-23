from pathlib import Path
import speech_recognition as sr

# Recognizerインスタンスを作成
recognizer = sr.Recognizer()

"""
GoogleのSpeechRecognitionライブラリを使用して音声を文字に変換する
"""


def voice_to_text(wavFile: Path) -> str:

    with sr.AudioFile(wavFile) as source:
        audio_data = recognizer.record(source)

        try:
            # 音声データをテキストに変換
            text = recognizer.recognize_google(
                audio_data, language="ja-JP")  # 日本語の場合
            return text
        except sr.UnknownValueError:
            return "Error! 音声が認識できませんでした"
        except sr.RequestError as e:
            return f"Error! APIに問題が発生しました: {e}"
