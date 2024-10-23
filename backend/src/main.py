from pathlib import Path
from fastapi import FastAPI, HTTPException, UploadFile
import uvicorn

from src.TaskState import TaskStatus
from src.video_to_audio_converter import extract_mp4_to_wav, is_mp4
from src.voice_to_text_extractor import voice_to_text

app = FastAPI()


async def async_write_file(uploaded_file: UploadFile, mp4_path: Path, wav_path: Path):
    # ファイルを一時ディレクトリに保存
    with open(mp4_path, "wb") as temp_file:
        temp_file.write(uploaded_file.file.read())

    # 非同期で変換処理を行い、待機する
    try:
        status, result = await extract_mp4_to_wav(mp4_path, wav_path)

        if status == TaskStatus.FAILED:
            return {"wav_file": ""}  # 失敗した場合
        else:
            return {"wav_file": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""
    # 以下を適切な場所に記載する
    # 一時的なファイルパスを設定
    tmp_mp4_path = f"/tmp/{file.filename}"
    tmp_wav_path = f"/tmp/{Path(file.filename).stem}.wav"

    async_write_file(file, tmp_mp4_path, tmp_wav_path)
    voice_to_text(tmp_wav_path)
"""


"""
##### 以下、API
"""


@app.get("/hello")
async def root():
    return {"message": "Hello World"}


@app.post("/mp4")
async def post_mp4(file: UploadFile):
    # mp4チェック
    if not is_mp4(file):
        raise HTTPException(
            status_code=400, detail="Invalid file type. Only MP4 files are allowed."
        )

    # 問題がなければ成功ステータスを返す
    return {"": ""}


@app.get("/text")
async def get_voice_to_text():
    return {"talk": "say Hello!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
