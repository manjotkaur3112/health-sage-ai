from dotenv import load_dotenv
load_dotenv()

# Way 1
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_mistralai import ChatMistralAI
from langchain_huggingface import ChatHuggingFace

# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")
# res = model.invoke("Tell me about Happy Raikoti")
# print(res.content)

# model = ChatGroq(model="openai/gpt-oss-120b")
# res = model.invoke("Tell me a joke")
# print(res.content)

# model = ChatMistralAI(model="mistral-large-latest")
# res = model.invoke("Tell me about modi")
# print(res.content)

# model = ChatHuggingFace(model="LH-Tech-AI/Apex-1.5-Instruct-350M")
# res = model.invoke("Tell me about Computer science branch")
# print(res.content)

from langchain.chat_models import init_chat_model

# # Way 2
# model = init_chat_model("google_genai:gemini-3.1-flash-lite")
# res = model.invoke("What is the best study branch in computer science")
# print(res.content[0]["text"]) 

# # Way 3 = it is the best for everyone because it is simple and easy to use
# model = init_chat_model("gemini-3.1-flash-lite",model_provider="google_genai")
# res = model.invoke("What is B.tech")
# print(res.content[0]["text"]) 

# model = init_chat_model("mistral-large-latest",model_provider="mistralai")
# res = model.invoke("Give me poem of sunset",temperature=0.1)
# print(res.content) 

# what is top P and top K, max_token, temperature

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_KEY"),
    max_new_tokens=1000,
)

model = ChatHuggingFace(llm=llm)
res = model.invoke("Tell me about AI Engineer")
print(res.content)
