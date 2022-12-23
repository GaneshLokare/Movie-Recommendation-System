import pandas as pd
from numpy import load
import sys
from movies.constants.data_ingestion_constants import preprocessed_data_path, cosine_sim_data_path
from movies.exception import MovieException


class Prediction:
    def __init__():
        pass

    def get_recommendations(movie):
        try:

            new_df = pd.read_csv(preprocessed_data_path)
            cosine_sim = load(cosine_sim_data_path)

            # get the index of title
            index = new_df[new_df['title'] == movie].index[0] 
            
            # Get the pairwsie similarity scores of all movies with that movie and Sort the movies based on the similarity scores
            distances = sorted(list(enumerate(cosine_sim[index])),reverse=True,key = lambda x: x[1])
            
            # Get the scores of the 5 most similar movies
            for i in distances[1:6]:
                print(new_df.iloc[i[0]].title)

        except  Exception as e:
                raise  MovieException(e,sys)

Prediction.get_recommendations('Thor')