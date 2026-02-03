import openai
from utils import read_file, write_file

openai.api_key = "YOUR_OPENAI_API_KEY"

topic = read_file("topic.txt")
prompt = f"Generate catchy YouTube video title, description, and 10 viral hashtags for topic: {topic}"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user", "content": prompt}]
)
seo_text = response.choices[0].message.content
write_file("seo.txt", seo_text)
print("SEO generated.")
