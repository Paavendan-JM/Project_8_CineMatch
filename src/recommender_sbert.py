from sentence_transformers import SentenceTransformer, util

class SBERTRecommender:
    def __init__(self, df):
        self.df = df.reset_index(drop=True)
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = self.model.encode(self.df['metadata'].tolist(), convert_to_tensor=True)

    def recommend(self, title, top_n=5):
        title = title.lower()
        matches = self.df[self.df['title'].str.lower() == title]
        if matches.empty:
            return ["Title not found."]
        
        idx = matches.index[0]
        query_embedding = self.embeddings[idx]
        similarities = util.pytorch_cos_sim(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort(descending=True)[1:top_n+1]

        return self.df.iloc[top_indices]['title'].tolist()
