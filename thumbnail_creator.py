from PIL import Image, ImageDraw, ImageFont
from utils import read_file

topic = read_file("topic.txt")

img = Image.new('RGB', (1280, 720), color=(255, 0, 0))
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((100, 300), topic, fill="white", font=font)
img.save("thumbnail.png")
print("Thumbnail saved.")
