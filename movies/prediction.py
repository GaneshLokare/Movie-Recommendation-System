import pandas as pd
from numpy import load
import sys
from movies.constants.data_ingestion_constants import preprocessed_data_path, cosine_sim_data_path
from movies.exception import MovieException

new_df = pd.read_csv(preprocessed_data_path)
class Prediction:
    def __init__():
        pass
        
    

    def get_recommendations(movie):
        try:

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


    def High_Rated_Movies():
        try:
            C= new_df['vote_average'].mean() # mean vote across the whole report
            m= new_df['vote_count'].quantile(0.9) # minimum votes required to be listed in the chart.
            q_movies = new_df.copy().loc[new_df['vote_count'] >= m] # filter out the movies that qualify for the chart

            def weighted_rating(x, m=m, C=C):
                v = x['vote_count']
                R = x['vote_average']
                # Calculation based on the IMDB formula
                return (v/(v+m) * R) + (m/(m+v) * C)
            
            q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
            #Sort movies based on score calculated above
            q_movies = q_movies.sort_values('score', ascending=False)
            #Print the top 10 movies
            print(q_movies[['title', 'vote_count', 'vote_average', 'score']].head(10))
        except  Exception as e:
                raise  MovieException(e,sys)

    def Popular_Movies():
        try: 
            pop= new_df.sort_values('popularity', ascending=False)
            print(pop['title'].head(6))
        except  Exception as e:
                raise  MovieException(e,sys)

    def Latest_Movies():
        try:
            latest= new_df.sort_values('release_date', ascending=False)
            print(latest[['title','release_date']].head(6))
        except  Exception as e:
                raise  MovieException(e,sys)  


Prediction.get_recommendations('Iron Man')
Prediction.High_Rated_Movies()
Prediction.Popular_Movies()
Prediction.Latest_Movies()