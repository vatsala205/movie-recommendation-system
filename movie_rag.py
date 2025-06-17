import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

def load_movie_csv(file_path):
    df = pd.read_csv(file_path)
    df.dropna(subset=["title", "genre", "description"], inplace=True)
    df['genre'] = df['genre'].str.lower()

    texts = [
        f"🎬 Title: {row['title']} | 🎭 Genre: {row['genre']} | 📝 Description: {row['description']}"
        for _, row in df.iterrows()
    ]

    return texts, df

def embed_texts(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(texts, show_progress_bar=True)

def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def get_top_movie_data(query, texts, embeddings, index, k=3):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vector = model.encode([query])
    scores, ids = index.search(query_vector, k)
    return [texts[i] for i in ids[0]]
