import pandas as pd
import ast


from movies.constants.data_ingestion_constants import movie_data_path,keywords_data_path,credits_data_path



movies = pd.read_csv(movie_data_path)
keywords = pd.read_csv(keywords_data_path)
credits = pd.read_csv(credits_data_path)

df = keywords.merge(movies, on = 'id')

data = df.merge(credits, on = 'id')

data = data.fillna("")

def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name']) 
    return L 

data['keywords'] = data['keywords'].apply(convert)
data['genres'] = data['genres'].apply(convert)
data['production_companies'] = data['production_companies'].apply(convert)
data['production_countries'] = data['production_countries'].apply(convert)
data['spoken_languages'] = data['spoken_languages'].apply(convert)

def convert_4(text):
    L = []
    j = 0
    for i in ast.literal_eval(text):
        L.append(i['name'])
        j += 1
        if j >= 4:
            break
    return L 

data['cast'] = data['cast'].apply(convert_4)

def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['department'] == 'Directing':
            L.append(i['name'])
            break
    return L

data['crew'] = data['crew'].apply(fetch_director)
