from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommender:
    def __init__(self, data):
        self.df = data.reset_index(drop=True)
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['metadata'])
        self.similarity = cosine_similarity(self.tfidf_matrix)

    def recommend(self, title, top_n=5):
        title_lower = title.lower()
        
        # Step 1: Find all movies with titles containing the input (partial match)
        partial_matches = self.df[self.df['title'].str.lower().str.contains(title_lower)]
        
        if not partial_matches.empty:
            # Exclude exact match if present
            exact_match = self.df[self.df['title'].str.lower() == title_lower]
            candidates = partial_matches[partial_matches.index != exact_match.index[0]] if not exact_match.empty else partial_matches
            
            # Return up to top_n titles from candidates
            recommendations = candidates['title'].head(top_n).tolist()
            if recommendations:
                return recommendations
        
        # Step 2: Fallback to original genre-based similarity if no partial title matches
        matches = self.df[self.df['title'].str.lower() == title_lower]
        if matches.empty:
            return ["Title not found."]
        
        idx = matches.index[0]
        query_genres = set(map(str.strip, self.df.loc[idx, 'listed_in'].split(',')))

        scores = list(enumerate(self.similarity[idx]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)

        recommendations = []
        for i, _ in scores:
            if i == idx:
                continue
            candidate_genres = set(map(str.strip, self.df.loc[i, 'listed_in'].split(',')))
            if query_genres & candidate_genres:
                recommendations.append(self.df.loc[i, 'title'])
            if len(recommendations) == top_n:
                break

        return recommendations
