import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="Personality AI Chatbot", page_icon="🎭", layout="wide")

PERSONALITIES = {
    "Funny": {
        "emoji": "😂",
        "avatar": "😂",
        "color": "#fbbf24",
        "color2": "#f59e0b",
        "desc": "Jokes, puns & playful sarcasm",
        "prompt": "You are a funny, witty assistant who loves jokes, puns, and playful sarcasm in every reply.",
    },
    "Angry": {
        "emoji": "😠",
        "avatar": "😠",
        "color": "#ef4444",
        "color2": "#dc2626",
        "desc": "Short-tempered but still helpful",
        "prompt": "You are a short-tempered, blunt assistant who replies with irritation and grumbling, but still gives useful answers.",
    },
    "Sad": {
        "emoji": "😢",
        "avatar": "😢",
        "color": "#60a5fa",
        "color2": "#3b82f6",
        "desc": "Melancholic, wistful tone",
        "prompt": "You are a melancholic, gloomy assistant who responds in a wistful, downbeat tone, sighing between thoughts.",
    },
    "Romantic": {
        "emoji": "💕",
        "avatar": "💕",
        "color": "#ec4899",
        "color2": "#db2777",
        "desc": "Flowery, heartfelt language",
        "prompt": "You are a romantic, poetic assistant who speaks in flowery, affectionate, heartfelt language.",
    },
    "Motivational": {
        "emoji": "🔥",
        "avatar": "🔥",
        "color": "#f97316",
        "color2": "#ea580c",
        "desc": "Energetic hype & inspiration",
        "prompt": "You are an energetic, motivational assistant who hypes up the user and inspires them with every reply.",
    },
}

if "personality" not in st.session_state:
    st.session_state.personality = None
if "messages" not in st.session_state:
    st.session_state.messages = []

model = ChatMistralAI(model="mistral-large-latest", temperature=0.9)

active = PERSONALITIES.get(st.session_state.personality)
accent = active["color"] if active else "#8b5cf6"
accent2 = active["color2"] if active else "#06b6d4"

st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');

            html, body, [class*="css"] {{
                font-family: 'Poppins', sans-serif;
            }}

            .stApp {{
                background: radial-gradient(circle at 20% 20%, rgba(139,92,246,0.15), transparent 40%),
                            radial-gradient(circle at 80% 0%, rgba(6,182,212,0.12), transparent 40%),
                            linear-gradient(135deg, #0b1120 0%, #0f172a 50%, #111827 100%);
            }}

            /* Kill the white top toolbar */
            header[data-testid="stHeader"] {{
                background: transparent !important;
            }}
            header[data-testid="stHeader"] * {{
                color: #f1f5f9 !important;
            }}

            .block-container {{
                padding-top: 2rem;
                max-width: 950px;
            }}

            .hero {{
                text-align: center;
                padding: 30px 10px 10px 10px;
            }}

            .hero h1 {{
                font-size: 46px;
                font-weight: 800;
                margin-bottom: 6px;
                background: linear-gradient(90deg, {accent}, {accent2});
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                letter-spacing: -1px;
            }}

            .hero p {{
                color: #cbd5e1 !important;
                font-size: 17px;
            }}

            .badge {{
                display: inline-block;
                padding: 6px 18px;
                border-radius: 999px;
                background: {accent}22;
                border: 1px solid {accent}55;
                color: {accent} !important;
                font-weight: 600;
                font-size: 14px;
                margin-bottom: 20px;
            }}

            /* Chat messages - force readable text everywhere inside */
            [data-testid="stChatMessage"] {{
                border-radius: 20px;
                padding: 14px 16px;
                margin-bottom: 14px;
                box-shadow: 0 4px 14px rgba(0,0,0,0.25);
            }}

            [data-testid="stChatMessage"] p,
            [data-testid="stChatMessage"] span,
            [data-testid="stChatMessage"] div {{
                color: #f1f5f9 !important;
            }}

            [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {{
                background: rgba(255,255,255,0.08) !important;
                border: 1px solid rgba(255,255,255,0.15);
            }}

            [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {{
                background: linear-gradient(135deg, {accent}26, {accent2}1a) !important;
                border: 1px solid {accent}40;
            }}

            /* Chat input box - the part that was pure white */
            [data-testid="stChatInput"] {{
                background: rgba(15, 23, 42, 0.9) !important;
                border-radius: 999px;
                border: 1px solid {accent}55 !important;
            }}

            [data-testid="stChatInput"] textarea {{
                color: #f1f5f9 !important;
                background: transparent !important;
            }}

            [data-testid="stChatInput"] textarea::placeholder {{
                color: #94a3b8 !important;
            }}

            [data-testid="stChatInput"] button svg {{
                fill: {accent} !important;
            }}

            section[data-testid="stSidebar"] {{
                background: rgba(10, 15, 30, 0.97);
                border-right: 1px solid rgba(148,163,184,0.12);
            }}

            section[data-testid="stSidebar"] * {{
                color: #f1f5f9 !important;
            }}

            .stButton > button {{
                border-radius: 14px;
                border: 1px solid {accent}55;
                background: {accent}18;
                color: #f1f5f9 !important;
                font-weight: 600;
                transition: all 0.2s ease;
            }}

            .stButton > button:hover {{
                border-color: {accent};
                background: {accent}33;
                transform: translateY(-1px);
            }}

            .persona-card {{
                border-radius: 18px;
                padding: 22px 16px;
                text-align: center;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.1);
                transition: all 0.25s ease;
                height: 100%;
            }}

            .persona-card:hover {{
                transform: translateY(-4px);
                border-color: rgba(255,255,255,0.3);
            }}

            .persona-emoji {{ font-size: 42px; margin-bottom: 8px; }}
            .persona-name {{ font-size: 18px; font-weight: 700; color: #f1f5f9 !important; margin-bottom: 4px; }}
            .persona-desc {{ font-size: 13px; color: #cbd5e1 !important; margin-bottom: 14px; }}

            .footer {{
                text-align: center;
                color: #64748b !important;
                font-size: 12px;
                margin-top: 40px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
        )

if active is None:
    st.markdown('<div class="hero"><h1>Personality AI Chatbot</h1><p>Choose a personality to start chatting</p></div>', unsafe_allow_html=True)
    columns = st.columns(len(PERSONALITIES))
    for column, (name, info) in zip(columns, PERSONALITIES.items()):
        with column:
            st.markdown(
                f'<div class="persona-card"><div class="persona-emoji">{info["emoji"]}</div><div class="persona-name">{name}</div><div class="persona-desc">{info["desc"]}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button("Select", key=f"pick_{name}", use_container_width=True):
                st.session_state.personality = name
                st.session_state.messages = [SystemMessage(content=info["prompt"])]
                st.rerun()
    st.stop()

st.markdown(
    f'<div style="text-align:center;"><span class="badge">{active["emoji"]} {st.session_state.personality} mode</span></div>',
    unsafe_allow_html=True,
)

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=active["avatar"]):
            st.markdown(msg.content)

prompt = st.chat_input("Type your message...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=active["avatar"]):
        placeholder = st.empty()
        with st.spinner("Thinking..."):
            try:
                res = model.invoke(st.session_state.messages)
                answer = res.content

                displayed = ""
                for chunk in answer.split(" "):
                    displayed += chunk + " "
                    placeholder.markdown(displayed + "▌")
                    time.sleep(0.01)
                placeholder.markdown(answer)

                st.session_state.messages.append(AIMessage(content=answer))
            except Exception as e:
                placeholder.empty()
                st.error(f"Something went wrong: {e}", icon="⚠️")
                st.session_state.messages.pop()

st.markdown('<div class="footer">Built with Streamlit • LangChain • Mistral AI</div>', unsafe_allow_html=True)