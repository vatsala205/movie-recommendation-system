from movie_rag import load_movie_csv, embed_texts, build_faiss_index, get_top_movie_data

file_path = "top_movies.csv"
texts, df = load_movie_csv(file_path)
embeddings = embed_texts(texts)
index = build_faiss_index(embeddings)

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

    # Genre match
    requested_genres = [genre for genre in GENRES if genre in user_input_lower]

    # Mood match
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


