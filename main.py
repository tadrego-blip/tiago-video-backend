from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import uuid
import subprocess

app = FastAPI()
VIDEO_DIR = "videos"
os.makedirs(VIDEO_DIR, exist_ok=True)

@app.post("/gerar-video/")
async def gerar_video(prompt: str):
    video_id = str(uuid.uuid4())
    output_path = os.path.join(VIDEO_DIR, f"{video_id}.mp4")

    # Cria vídeo simples com o texto do prompt (placeholder)
    subprocess.run([
        "ffmpeg",
        "-f", "lavfi",
        "-i", "color=c=black:s=1080x1920:d=5",
        "-vf", f"drawtext=text='{prompt}':fontcolor=white:fontsize=60:x=(w-text_w)/2:y=(h-text_h)/2",
        "-pix_fmt", "yuv420p",
        output_path
    ])

    return FileResponse(output_path, media_type="video/mp4", filename=f"{video_id}.mp4")
