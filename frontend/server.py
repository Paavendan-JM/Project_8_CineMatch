from flask import Flask, request, jsonify, send_from_directory
import os
import sys

# Add root directory to path to import src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.preprocess import load_and_clean_data
from src.recommender import Recommender

app = Flask(__name__, static_folder='.', static_url_path='')

# Load data and model once
df = load_and_clean_data(os.path.join('..', 'data', 'netflix.csv'))
reco = Recommender(df)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

@app.route('/script.js')
def serve_js():
    return send_from_directory('.', 'script.js')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    title = data.get('title', '')
    titles = reco.recommend(title)

    if titles == ["Title not found."]:
        return jsonify([])

    rows = []
    for t in titles:
        movie = df[df['title'] == t].iloc[0]
        rows.append({
            'title': movie.get('title', '-'),
            'genre': movie.get('listed_in', '-'),
            'description': movie.get('description', '-'),
            'actors': movie.get('top_cast', '-'),
            'director': movie.get('director', '-')
        })

    return jsonify(rows)


if __name__ == '__main__':
    app.run(debug=True)
