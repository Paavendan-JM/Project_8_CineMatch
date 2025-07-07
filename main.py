from src.preprocess import load_and_clean_data
from src.recommender import Recommender

if __name__ == "__main__":
    path = 'data/netflix.csv'
    df = load_and_clean_data(path)
    reco = Recommender(df)

    movie = input("Enter a movie/show title: ")
    recommendations = reco.recommend(movie)

    print("\nTop Recommendations:")
    for r in recommendations:
        print("-", r)
