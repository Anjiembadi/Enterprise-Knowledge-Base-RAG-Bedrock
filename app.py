import streamlit as st
from backend import get_answer

st.set_page_config(page_title="Enterprise Knowledge Assistant", page_icon="📚", layout="centered")

st.title("📚 Enterprise Knowledge Base Q&A")
st.write("Ask questions about internal company policies and documents.")

query = st.text_input("Ask your question:")

if st.button("Submit"):
    if query.strip():
        with st.spinner("Searching knowledge base..."):
            answer, sources = get_answer(query)

        st.subheader("Answer")
        st.write(answer)

        if sources:
            st.subheader("Sources")
            for src in sources:
                st.write(f"- {src}")
    else:
        st.warning("Please enter a question.")