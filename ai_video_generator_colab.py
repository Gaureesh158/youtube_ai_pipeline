import os
from utils import make_folder, read_file, split_segments

make_folder("clips")

script_text = read_file("script_segments.txt")
segments = split_segments(script_text)

for i, seg in enumerate(segments):
    prompt = seg[:200]  # Short prompt for AI visuals
    output_file = f"clips/clip_{i}.mp4"
    
    # Placeholder: Colab AI video generation code
    # generate_video_clip(prompt=prompt, duration=10, fps=24, output=output_file)
    
    print(f"Generated clip: {output_file}")
