from flask import Flask,request, jsonify, render_template
import pandas as pd
from numpy import load
import sys
from movies.constants.data_ingestion_constants import preprocessed_data_path, cosine_sim_data_path
from movies.exception import MovieException

new_df = pd.read_csv(preprocessed_data_path)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie_recommendation',methods=['POST'])

def get_recommendations():
    req = request.form.to_dict()
    movie_title = req['movie']
    cosine_sim = load(cosine_sim_data_path)

    # get the index of title
    index = new_df[new_df['title'] == movie_title].index[0] 
            
    # Get the pairwsie similarity scores of all movies with that movie and Sort the movies based on the similarity scores
    distances = sorted(list(enumerate(cosine_sim[index])),reverse=True,key = lambda x: x[1])
            
    # Get the scores of the 5 most similar movies
    movies = []
    for i in distances[1:6]:
        movies.append(new_df.iloc[i[0]].title)
    return render_template('output.html',movies = movies )

        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)