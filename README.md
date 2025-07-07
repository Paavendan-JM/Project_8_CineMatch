Movie Recommendation System

A Flask-based movie recommendation web app using TF-IDF similarity on movie metadata.

Features

- Search movie/show by title
- Get top 5 recommended movies/shows based on metadata similarity
- Filtered and ranked results with title, year, genre, description, actors, and director
- Simple frontend with HTML, CSS, and JavaScript
- Backend API built with Flask

Setup

1. Clone the repo

git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Create & activate virtual environment (optional but recommended)

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the Flask server

python server.py

5. Open your browser and go to

http://127.0.0.1:5000

Usage

- Enter a movie or show title in the input box
- Click the button or press Enter
- See top 5 recommended titles in a table below

Project Structure

data/
    netflix.csv         # Dataset CSV file
src/
    preprocess.py       # Data cleaning and loading
    recommender.py      # Recommendation logic using TF-IDF
server.py               # Flask backend server
index.html              # Frontend HTML page
style.css               # CSS styling
script.js               # Frontend JS fetching recommendations
requirements.txt        # Python dependencies
README.txt              # This file

Dependencies

- Flask
- pandas
- scikit-learn

License

MIT License

Enjoy exploring movie recommendations!
