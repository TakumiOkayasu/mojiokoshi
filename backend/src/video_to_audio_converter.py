import asyncio
from pathlib import Path
import subprocess

from fastapi import UploadFile
import ffmpeg

from src.TaskState import TaskStatus

"""
渡されたファイルがmp4か判定する
"""


def is_mp4(mp4file: UploadFile) -> bool:

    if mp4file.content_type != "video/mp4":
        return False

    try:
        probe = ffmpeg.probe(mp4file)
        return probe['format']['format_name'] == 'mov,mp4,m4a,3gp,3g2,mj2'
    except ffmpeg.Error:
        return False


"""
mp4 -> wavに変換する
変換後のパスを返す
"""


async def extract_mp4_to_wav(mp4_path: Path, wav_path: str) -> {TaskStatus, Path}:

    command = [
        "ffmpeg",
        "-i", str(mp4_path),
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        str(wav_path)
    ]

    task_status = TaskStatus()

    try:
        process = await asyncio.create_subprocess_exec(*command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        await process.communicate()

        # タスク完了後にステータスを変更
        if process.returncode == 0:
            task_status = TaskStatus.COMPLETED
        else:
            task_status = TaskStatus.FAILED

        return task_status, Path(wav_path)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e.stderr.decode()}")
        return TaskStatus.FAILED, Path("NotFound")
