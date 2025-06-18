from movie_rag import build_faiss_index
import pickle

# Load precomputed data
with open("texts.pkl", "rb") as f:
    texts = pickle.load(f)

with open("embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

index = build_faiss_index(embeddings)

# GENRE and MOOD logic (unchanged)
GENRES = {
    "action", "drama", "thriller", "romance", "comedy",
    "sci-fi", "horror", "crime", "adventure", "mystery",
    "animation", "fantasy", "biography", "family", "war"
}

MOOD_MAP = {
    "feel-good": ["comedy", "family", "romance", "animation", "uplifting"],
    "intense": ["thriller", "action", "crime", "suspense"],
    "dark": ["horror", "crime", "drama", "psychological"],
    "uplifting": ["inspiring", "biography", "drama", "hope"],
    "romantic": ["romance", "love", "relationship"],
    "funny": ["comedy", "humor", "satire"]
}

from movie_rag import get_top_movie_data  # moved here to avoid cyclic imports

def extract_requested_fields(user_input, top_results):
    user_input_lower = user_input.lower()

    requested_genres = [genre for genre in GENRES if genre in user_input_lower]

    requested_moods = [mood for mood in MOOD_MAP if mood in user_input_lower]
    mood_keywords = []
    for mood in requested_moods:
        mood_keywords.extend(MOOD_MAP[mood])

    filtered = top_results

    if requested_genres:
        filtered = [
            movie for movie in filtered
            if any(genre in movie.lower() for genre in requested_genres)
        ]

    if mood_keywords:
        filtered = [
            movie for movie in filtered
            if any(keyword in movie.lower() for keyword in mood_keywords)
        ]

    return filtered if filtered else top_results