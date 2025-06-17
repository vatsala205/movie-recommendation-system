import streamlit as st
from main import get_top_movie_data, texts, embeddings, index, extract_requested_fields

st.title("🎥 Movie Recommender Chatbot")

user_input = st.text_input("Ask about a type of movie...")

if user_input:
    top_results = get_top_movie_data(user_input, texts, embeddings, index)
    results = extract_requested_fields(user_input, top_results)

    st.markdown("### 🎬 Top Matches")
    for res in results:
        st.markdown(f"- {res}")
