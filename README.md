"# Movie Recommendation System" 


# 🎥 Movie Recommender Chatbot

A conversational movie recommendation system powered by vector search and local embeddings. This chatbot allows users to request movie suggestions based on **genre**, **mood**, or natural language queries — all without needing access to external APIs or cloud services.

## 🧠 Features

- 🎬 **Genre & Mood-Based Filtering** – Filter results by genre (e.g., "drama", "sci-fi") or mood (e.g., "feel-good", "intense").
- 🤖 **LLM-Powered Matching** – Queries are transformed into embeddings to semantically match movies from a local dataset.
- 🗂️ **Local Vector Store** – Uses **FAISS** for fast, offline similarity search on movie descriptions.
- 🌐 **Interactive Web UI** – Built with **Streamlit** for a clean, user-friendly interface.
- 💾 **Fully Local Setup** – No API keys or internet dependency after setup.

## 📁 Project Structure

```bash

Carinfo\_Chatbot/
│
├── top\_movies.csv                # Local dataset of top movies
├── main.py                       # Core logic: load data, create embeddings, build index
├── movie\_rag.py                  # RAG helper functions
├── streamlit\_app.py              # Frontend app using Streamlit
├── requirements.txt              # Python dependencies
└── README.md                     # This file

```

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender-chatbot.git
   cd movie-recommender-chatbot


2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open your browser at `http://localhost:8501`.

### Sample Prompts:

* `"Suggest me a drama movie"`
* `"I want something uplifting and emotional"`
* `"Any intense thrillers?"`

## 📊 Tech Stack

* Python 🐍
* Streamlit 🌐
* FAISS 🔍
* Sentence Transformers (for embeddings) 🧠
* Pandas 📊

## ✨ Future Enhancements

* [ ] Add support for year or era-based filtering
* [ ] Integrate actor/director info if dataset is expanded
* [ ] User ratings and feedback loop
* [ ] Use multilingual embeddings for broader access

## 📌 License

This project is licensed under the MIT License. Feel free to use and modify it for your own applications!
]

