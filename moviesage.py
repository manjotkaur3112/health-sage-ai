from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
import json


model = ChatMistralAI(model="mistral-small-2603")


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are MovieSage, an AI movie information extraction and summarization bot.

Your job is to:

1. Read a raw paragraph about a movie.
2. Extract important structured information.
3. Generate a clean and concise summary.
4. Return ONLY valid JSON.
5. Do not add markdown, explanations, or ```json blocks.

The JSON must follow exactly this structure:

{{
    "title": "",
    "year": null,
    "genre": [],
    "director": "",
    "cast": [],
    "language": "",
    "rating": null,
    "duration": "",
    "summary": "",
    "keywords": []
}}

Rules:
- If information is missing, use null for single values.
- Use [] for missing lists.
- Do not invent information.
- The summary should be 2-4 sentences.
- Extract only information present in the input.
"""
    ),
    (
        "human",
        """
Extract information from the following movie paragraph:

{movie_text}
"""
    )
])


para = input("Give your para about the movie")
final_prompt = prompt.invoke({"movie_text": para})
res = model.invoke(final_prompt)
print(res.content)