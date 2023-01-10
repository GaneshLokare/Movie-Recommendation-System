# Movie-Recommendation-System


## Description:
A movie recommendation system is a tool that suggests movies to users based on their preferences and viewing history. Such a system can be built using a variety of techniques, including collaborative filtering, content-based filtering, and hybrid approaches that combine the two. This is a content-based recommendations.

This project is a movie recommendation system that uses a data from TMDB website. In this project I have build a pipeline using API which is automatically fetching required data from TMDB website. For fetching automalically data I have used a windows shcedular. After fetching data, system will preprocess and train model. Here model training means computing cosine similarity matrix and recommend movies based on the similarity.

Once the model is trained, it can be used to make personalized recommendations to users based on their preferences. The system also extended with additional features such as High rated movies recommendations, popular movies recommendations, and latest movies recommendations.

Some of the technical aspects of the project include the following:

- Fetching data using API.
- Data preprocessing, including cleaning and formatting the data,
- Model selection and training,
- Building a web-based user interface to interact with the recommendation system.

## How to run the project?
1) Clone or download this repository to your local machine.
2) Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt
3) Get your API key from https://www.themoviedb.org/.
4) Replace YOUR_API_KEY in data ingintion constant and save it.
5) set a windows task shedular. [Watch video] (https://www.youtube.com/watch?v=4n2fC97MNac) 
5) Open your terminal/command prompt from your project directory and run the file main.py by executing the command python app.py.
Go to your browser and type http://192.168.181.65:8080  in the address bar.

## Dependencies:
- pandas
- numpy
- from-root
- DateTime
- requests
- astdump
- nltk
- regex
- Flask

