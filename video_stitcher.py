from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    concatenate_videoclips,
    CompositeVideoClip,
    TextClip
)
from utils import make_folder
import os

# ---------------- SETTINGS ----------------
MIN_DURATION = 8 * 60    # 8 minutes
MAX_DURATION = 15 * 60   # 15 minutes
FPS = 24
CTA_TEXT = "Like 👍 | Subscribe 🔔 | Share ❤️"

# ---------------- FOLDERS ----------------
make_folder("clips")
make_folder("voice")
make_folder("music")

# ---------------- LOAD FILES ----------------
video_files = sorted(os.listdir("clips"))
voice_files = sorted(os.listdir("voice"))

if not video_files or not voice_files:
    raise Exception("❌ clips/ ya voice/ folder empty hai")

clips = []
total_duration = 0
index = 0

# ---------------- BUILD VIDEO ----------------
while total_duration < MIN_DURATION:
    v = video_files[index % len(video_files)]
    a = voice_files[index % len(voice_files)]

    clip = VideoFileClip(f"clips/{v}")
    voice = AudioFileClip(f"voice/{a}")

    clip = clip.set_audio(voice)

    txt_clip = (
        TextClip(CTA_TEXT, fontsize=42, color="yellow", font="Arial-Bold")
        .set_duration(clip.duration)
        .set_position(("center", "bottom"))
    )

    final_clip = CompositeVideoClip([clip, txt_clip])
    clips.append(final_clip)

    total_duration += final_clip.duration
    index += 1

    if total_duration >= MAX_DURATION:
        break

# ---------------- CONCAT ----------------
final_video = concatenate_videoclips(clips, method="compose")

# ---------------- BACKGROUND MUSIC ----------------
bg_music_path = "music/bg_music.mp3"

if os.path.exists(bg_music_path):
    bg_music = AudioFileClip(bg_music_path)
    bg_music = bg_music.volumex(0.18)

    if bg_music.duration < final_video.duration:
        bg_music = bg_music.audio_loop(duration=final_video.duration)

    final_video = final_video.set_audio(
        final_video.audio.volumex(1.0).fx(
            lambda a: a.overlay(bg_music)
        )
    )

# ---------------- EXPORT ----------------
output_file = "final_video.mp4"
final_video.write_videofile(
    output_file,
    fps=FPS,
    codec="libx264",
    audio_codec="aac"
)

print(f"✅ FINAL LONG VIDEO READY: {output_file}")
print(f"⏱ Duration: {int(total_duration/60)} minutes")
