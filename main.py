from movies.data_ingestion.fetch_movies_data import movies_data
from movies.data_ingestion.fetch_keywords_data import keywords_data
from movies.data_ingestion.fetch_credits_data import credits_data
from movies.data_preprocessing.preprocessing import Preprocessing
from movies.training import Train_model

movies_data.fetch_data()
keywords_data.fetch_data()
credits_data.fetch_data()
Preprocessing.data_preprocessing()
#Train_model.train()