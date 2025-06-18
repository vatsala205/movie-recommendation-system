from movie_rag import build_faiss_index, get_top_movie_data
import pickle
import faiss

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

def extract_requested_fields(user_input, top_results):
    user_input_lower = user_input.lower()

    requested_genres = [genre for genre in GENRES if genre in user_input_lower]
    requested_moods = [mood for mood in MOOD_MAP if mood in user_input_lower]

    mood_keywords = []
    for mood in requested_moods:
        mood_keywords.extend(MOOD_MAP[mood])

    filtered = top_results

    if requested_genres:
        filtered = [movie for movie in filtered if any(g in movie.lower() for g in requested_genres)]

    if mood_keywords:
        filtered = [movie for movie in filtered if any(m in movie.lower() for m in mood_keywords)]

    return filtered if filtered else top_results


# 💡 Only runs if you execute this file directly
# if __name__ == "__main__":
#     from movie_rag import load_movie_csv, embed_texts
#
#     texts, df = load_movie_csv("top_movies.csv")  # Replace with your CSV name
#     embeddings = embed_texts(texts)
#
#     # Save new files
#     with open("texts.pkl", "wb") as f:
#         pickle.dump(texts, f)
#
#     with open("embeddings.pkl", "wb") as f:
#         pickle.dump(embeddings, f)
#
#     index = build_faiss_index(embeddings)
#     faiss.write_index(index, "movie_index.faiss")
#
#     print("✅ Pickle and FAISS index files created successfully.")
