from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
from utils import make_folder
import os

make_folder("clips")  # Ensure folder exists

clips = []
voice_files = sorted(os.listdir("voice"))
video_files = sorted(os.listdir("clips"))

for v, a in zip(video_files, voice_files):
    clip = VideoFileClip(f"clips/{v}")
    voice = AudioFileClip(f"voice/{a}")
    clip = clip.set_audio(voice)
    
    txt_clip = TextClip("Like, Subscribe & Share ❤️", fontsize=40, color='yellow')
    txt_clip = txt_clip.set_duration(clip.duration).set_position(("center","bottom"))
    
    final_clip = CompositeVideoClip([clip, txt_clip])
    clips.append(final_clip)

bg_music = AudioFileClip("music/bg_music.mp3")
final_video = concatenate_videoclips(clips)
final_video = final_video.set_audio(bg_music.volumex(0.2))

final_video.write_videofile("final_video.mp4", fps=24)
print("Final video created: final_video.mp4")
