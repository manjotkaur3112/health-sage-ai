from pyexpat import model

from dotenv import load_dotenv
load_dotenv()
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# prompt=input("YOU:")
model = ChatMistralAI(model="mistral-large-latest",temperature=0.9)
# res=model.invoke(prompt)
# print("BOT:",res.content)

print("_______Welcome type 0 to exit to Chatbot_______")
print("AI Chatbot")
print("1. Funny")
print("2. Angry")
print("3. Sad")
print("4. Romantic")
print("5. Motivational")

personality = {
    "1": "You are a funny",
    "2": "",
    "3": "",
    "4": "",
    "5": ""
}

choice = input("Enter your personality(1-5):")
if choice not in personality:
    print("Invalid choice")
    exit()


messages=[SystemMessage(content=personality[choice])]
while True:
    prompt=input("YOU:")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        print("Thank you for using Chatbot")
        break
    res=model.invoke(messages)
    messages.append(AIMessage(content=res.content))
    print(messages)
    print("BOT:",res.content)
