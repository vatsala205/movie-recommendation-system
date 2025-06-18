import streamlit as st
import faiss
import pickle
from movie_rag import get_top_movie_data
from main import extract_requested_fields

# Plain data loading (no caching decorator)
def load_data():
    with open("texts.pkl", "rb") as f:
        texts = pickle.load(f)
    with open("embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)
    index = faiss.read_index("movie_index.faiss")  # Requires saved index file
    return texts, embeddings, index

texts, embeddings, index = load_data()

st.title("🎥 Movie Recommender Chatbot")

user_input = st.text_input("Ask about a type of movie...")

if user_input:
    top_results = get_top_movie_data(user_input, texts, embeddings, index)
    results = extract_requested_fields(user_input, top_results)

    st.markdown("### 🎬 Top Matches")
    for res in results:
        st.markdown(f"- {res}")
