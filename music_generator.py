import requests
from utils import make_folder

make_folder("music")

# Placeholder: free AI music URL
music_url = "https://example.com/free_music.mp3"
r = requests.get(music_url)
with open("music/bg_music.mp3", "wb") as f:
    f.write(r.content)
print("Background music saved.")
