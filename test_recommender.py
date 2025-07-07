from src.preprocess import load_and_clean_data
from src.recommender import Recommender

def test_recommender():
    df = load_and_clean_data('data/netflix.csv')
    reco = Recommender(df)

    tests = {
    "GoodFellas": ["Raging Bull", "The Irishman"],
    "Inglourious Basterds": ["Django Unchained", "The Hateful Eight"],
    "Inception": ["Interstellar", "Tenet"],
    "The Matrix": ["The Matrix Reloaded", "The Matrix Revolutions"],
}



    for title, expected in tests.items():
        result = reco.recommend(title)
        hits = [movie for movie in result if movie in expected]
        accuracy = round(len(hits) / len(expected) * 100, 2)
        print(f"{title}: {accuracy}% match ({hits})")

if __name__ == "__main__":
    test_recommender()
