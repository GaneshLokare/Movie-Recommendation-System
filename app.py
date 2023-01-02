from flask import Flask,request, jsonify, render_template
import pandas as pd
from numpy import load
from movies.constants.data_ingestion_constants import preprocessed_data_path, cosine_sim_data_path


new_df = pd.read_csv(preprocessed_data_path)
new_df['title_low'] = new_df['title'].apply(lambda x: x.lower())
new_df['title_low'] = new_df['title_low'].apply(lambda x: x.replace(' ',''))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/movie_recommendation',methods=['POST'])

def get_recommendations():
    req = request.form.to_dict()
    movie_title = req['movie']
    movie_title = movie_title.lower().replace(' ','')
    cosine_sim = load(cosine_sim_data_path)

    try:
        # get the index of title
        index = new_df[new_df['title_low'] == movie_title].index[0]
    
            
        # Get the pairwsie similarity scores of all movies with that movie and Sort the movies based on the similarity scores
        distances = sorted(list(enumerate(cosine_sim[index])),reverse=True,key = lambda x: x[1])
            
        # Get the scores of the 5 most similar movies
        movies = []
        for i in distances[1:6]:
            movies.append(new_df.iloc[i[0]].title)
        return render_template('index.html',movies = movies )

    except:
        return render_template('message.html')

@app.route('/Popular_Movies')
def Popular_Movies():
    pop= new_df.sort_values('popularity', ascending=False)
    popular_movies = list(pop['title'].head(10))
    return render_template('popular.html',popular_movies = popular_movies )

@app.route('/Latest_Movies')
def Latest_Movies():
        latest= new_df.sort_values('release_date', ascending=False)
        latest_movies = list(latest['title'].head(10))
        return render_template('latest.html',latest_movies = latest_movies )
        

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)