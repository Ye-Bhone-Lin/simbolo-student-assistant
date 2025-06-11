import streamlit as st
from search_engine import GenerateOutput

st.set_page_config(page_title="Simbolo Student Assistant", layout="centered")
st.title("Simbolo Student Assistant")

es = st.secrets.general.ELASTIC_SEARCH_API_KEY
gr = st.secrets.general.GROQ_API_KEY


st.markdown("""
<style>
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
    max-width: 700px;
    margin: 0 auto 20px auto;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.chat-message {
    padding: 12px 18px;
    border-radius: 20px;
    max-width: 70%;
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    line-height: 1.4;
    font-size: 16px;
    white-space: pre-wrap;
}

.user-message {
    background-color: #4caf50;  /* fresh green */
    color: white;
    align-self: flex-end;
    border-bottom-right-radius: 4px;
}

.bot-message {
    background-color: #f1f0f0;  /* light gray */
    color: #333;
    align-self: flex-start;
    border-bottom-left-radius: 4px;
}

input[type="text"] {
    padding: 12px;
    font-size: 16px;
    border-radius: 10px;
    border: 1.5px solid #ccc;
    width: 100%;
    box-sizing: border-box;
    margin-bottom: 8px;
}

.stButton>button {
    background-color: #4caf50;
    color: white;
    font-weight: bold;
    padding: 10px 18px;
    border-radius: 10px;
    border: none;
    width: 100%;
    cursor: pointer;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    role = msg["role"]
    content = msg["content"]
    css_class = "user-message" if role == "user" else "bot-message"
    st.markdown(f"<div class='chat-message {css_class}'>{content}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your question here:", "", key="input")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.spinner("Simbolo Assistant is typing..."):
        bot_response = GenerateOutput.model_generate(user_input)
    st.session_state["messages"].append({"role": "bot", "content": bot_response})
    st.markdown(f"<div class='chat-message bot-message'>{bot_response}</div>", unsafe_allow_html=True)
