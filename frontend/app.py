import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="MedRAG AI",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MedRAG AI")
st.caption("AI Powered Medical Report Explainer")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:

    st.header("Upload Report")

    uploaded_file = st.file_uploader(
        "Choose Report",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    if st.button("Process Report"):

        if uploaded_file:

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    uploaded_file.type
                )
            }

            response = requests.post(
                f"{FASTAPI_URL}/upload",
                files=files
            )

            if response.status_code == 200:
                st.success(
                    "Report Processed Successfully"
                )
            else:
                st.error(
                    response.text
                )

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input(
    "Ask about your report..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = requests.post(
        f"{FASTAPI_URL}/explain",
        json={
            "question": prompt
        }
    )

    answer = response.json()["answer"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.write(answer)