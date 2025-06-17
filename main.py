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

def extract_requested_fields(user_input, top_results):
    user_input_lower = user_input.lower()

    # Extract genre from user input
    requested_genres = [genre for genre in GENRES if genre in user_input_lower]

    # Filter top results by requested genre(s)
    if requested_genres:
        filtered_results = [
            movie for movie in top_results
            if any(genre in movie.lower() for genre in requested_genres)
        ]
        return filtered_results if filtered_results else top_results

    return top_results

