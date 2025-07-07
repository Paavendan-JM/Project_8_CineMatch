import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df = df[['title', 'director', 'cast', 'listed_in', 'description']]
    df.dropna(inplace=True)

    df['top_cast'] = df['cast'].apply(lambda x: ', '.join(x.split(', ')[:3]))

    # Priority: description > genre > director > cast
    df['metadata'] = df['description'] + ' ' + df['listed_in'] + ' ' + df['director'] + ' ' + df['top_cast']
    df['metadata'] = df['metadata'].str.lower()

    return df
