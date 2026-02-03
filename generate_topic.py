import random

hinglish_topics = [
    "This AI tool can earn you ₹50,000 per month without coding",
    "Top 5 AI websites that Indians are secretly using in 2026",
    "This free AI can replace 5 hours of your daily work",
    "People are using this AI tool to make money online",
    "This AI website is better than ChatGPT for earning"
]

hindi_topics = [
    "ये AI टूल आपको घर बैठे पैसे कमा कर दे सकता है",
    "ये AI आपकी नौकरी खतरे में डाल सकता है",
    "ये फ्री AI टूल आपको अमीर बना सकता है",
    "ये AI वेबसाइट बहुत कम लोग जानते हैं",
]

def generate_topic(video_number):
    # 80% Hinglish, 20% Hindi
    if video_number % 5 == 0:
        return random.choice(hindi_topics)
    else:
        return random.choice(hinglish_topics)
