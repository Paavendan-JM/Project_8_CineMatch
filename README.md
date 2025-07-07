# Movie Recommendation System

This project is an **ML-powered movie recommendation system that uses TF-IDF vectorization** and **cosine similarity** to find similar movies based on their metadata (title, genre, director, cast). It prioritizes intelligent content-based recommendations using classical ML techniques without deep learning or embeddings. A simple **Flask API** powers the backend, while a lightweight JavaScript-based UI acts as an interface to query the model and display results.

## Features
 - Enter any movie or show title to receive intelligent recommendations
 - Uses a machine learning-based hybrid algorithm leveraging TF-IDF vectorization and cosine similarity to match titles based on semantic relevance
 - Prioritizes partial title matches, director, genre overlap (≥75%), and top-billed actors to improve recommendation quality
 - Filters results by country and type (Movie / TV Show) to ensure contextual accuracy
 - Displays detailed metadata: Title, Year, Genre, Description, Actors, and Director
 - Designed to handle large datasets efficiently using vectorized operations and optimized similarity search

## Tech Stack

- Python 3.12+
- Flask (backend API)
- pandas, scikit-learn (TF-IDF, similarity)
- Vanilla JavaScript (frontend)
- HTML & CSS for UI

## Project Structure

frontend/
├── index.html
├── style.css
├── script.js
└── server.py # Flask backend
src/
├── preprocess.py # Data loading and cleaning
└── recommender.py # Recommendation logic
data/
└── netflix.csv # Dataset (Netflix movies and shows metadata)


## Setup & Run

1. Clone the repo:
   ```bash
   git clone <repo_url>
   cd <repo_folder>


2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the server:
    ```bash
    cd frontend
    python server.py


Notes
 - Ensure netflix.csv dataset is present in the data folder.
 - Customize and improve recommendation logic as needed.
 - UI is minimal and can be enhanced with frameworks if desired.
