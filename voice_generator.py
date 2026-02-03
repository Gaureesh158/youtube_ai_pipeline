from gtts import gTTS
from utils import make_folder, read_file, split_segments

make_folder("voice")

script_text = read_file("script_segments.txt")
segments = split_segments(script_text)

for i, seg in enumerate(segments):
    tts = gTTS(text=seg, lang="hi")
    tts.save(f"voice/voice_{i}.mp3")
    print(f"Voice saved: voice_{i}.mp3")
