import pandas as pd
import requests
from pandas.io.json import json_normalize



class movies_data:
    def __init__():
        pass

    def fetch_data():
        try:

            df = pd.DataFrame()

            for i in range(start_index,end_index):
                res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(i))
                array = res.json()
                temp_df = json_normalize(array)
                df = df.append(temp_df,ignore_index=True)

            df1 = df[['genres', 'id', 'original_language',
                'original_title', 'overview', 'popularity', 'production_companies',
                'production_countries', 'release_date',
                'spoken_languages', 'tagline', 'title', 'vote_average',
                'vote_count']]

            df1.to_csv('movies1.csv',index = False)

        except  Exception as e:
                raise  QuoraException(e,sys)