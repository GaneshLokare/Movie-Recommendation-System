import pandas as pd
import ast
import os.path as path
from regex import regex as re
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from movies.exception import MovieException
from movies.logger import logging
import sys
import warnings
warnings.filterwarnings('ignore')


from movies.constants.data_ingestion_constants import movie_data_path,keywords_data_path,credits_data_path,preprocessed_data_path,start_index, end_index



class Preprocessing:
    def __init__():
        pass
    def data_preprocessing():
        try:
            pre = pd.read_csv(preprocessed_data_path)
            rows = pre.shape[0]
            movies = pd.read_csv(movie_data_path,skiprows = [i for i in range(1, rows+1) ])
            keywords = pd.read_csv(keywords_data_path,skiprows = [i for i in range(1, rows+1) ])
            credits = pd.read_csv(credits_data_path,skiprows = [i for i in range(1, rows+1) ],on_bad_lines='skip')


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

            data['release_date'] = data['release_date'].apply(lambda x: x[:4])
            

            data['genres'] = data['genres'].apply(lambda x: ' '.join(x))
            data['keywords'] = data['keywords'].apply(lambda x: ' '.join(x))
            data['production_companies'] = data['production_companies'].apply(lambda x: ' '.join(x))
            data['spoken_languages'] = data['spoken_languages'].apply(lambda x: ' '.join(x))
            data['spoken_languages'] = data['spoken_languages'].apply(lambda x: ' '.join(x))
            data['cast'] = data['cast'].apply(lambda x: ' '.join(x))
            data['crew'] = data['crew'].apply(lambda x: ' '.join(x))

            data['text'] = data['genres'] + data['keywords'] + data['original_language'] + data['overview'] + data['production_companies'] + data['spoken_languages'] +data['tagline']+ data['cast'] + data['crew']

            new_data = data[['id','title','text','popularity','release_date','vote_average','vote_count']]

            # remove all special characters and lower the cases
            def remove_special_characters(text):
                text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
                return text

            new_data["text"] = new_data["text"].apply(lambda x: remove_special_characters (x))


            # lemmetization
            def lem_words(text):
                lst_text = text.split()
                lem = nltk.stem.wordnet.WordNetLemmatizer()
                lst_text = [lem.lemmatize(word) for word in lst_text]
                text = " ".join(lst_text)
                return text

            new_data["text"] = new_data["text"].apply(lambda x: lem_words (x))

           
            data_path = path.abspath(path.join(preprocessed_data_path))
            logging.info("Preprocessing done")
            new_data.to_csv(data_path, mode= 'a', index=False, header= False)
        except  Exception as e:
                raise  MovieException(e,sys)

