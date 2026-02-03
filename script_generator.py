import openai
from utils import read_file, write_file, split_segments

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_script(topic):
    prompt = f"""
    Generate a Hindi YouTube video script for topic: '{topic}'.
    The script should be 8–15 minutes long, divided into 45–60s segments.
    Include visual prompts for AI-generated animations.
    Add CTA: 'Like, Subscribe & Share' at start and end.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content":prompt}]
    )
    script = response.choices[0].message.content.strip()
    segments = [line.strip() for line in script.split("\n\n") if line.strip()]
    write_file("script_segments.txt", "\n---\n".join(segments))
    print("Script Generated.")

if __name__ == "__main__":
    topic = read_file("topic.txt")
    generate_script(topic)
