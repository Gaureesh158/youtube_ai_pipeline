import openai
from utils import write_file

import os
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_topic():
    prompt = "Give me a trending Hindi topic for YouTube video in 2026 (viral & interesting)"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )
    topic = response.choices[0].message.content.strip()
    write_file("topic.txt", topic)
    print("Topic Generated:", topic)

if __name__ == "__main__":
    generate_topic()
