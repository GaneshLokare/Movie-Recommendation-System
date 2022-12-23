import pandas as pd
import os.path as path
from numpy import save
import sys
from movies.exception import MovieException
from movies.logger import logging
from movies.constants.data_ingestion_constants import preprocessed_data_path, cosine_sim_data_path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class Train_model:
    def __init__():
        pass

    def train():
        try:


            new_df = pd.read_csv(preprocessed_data_path)

            #Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
            tfidf = TfidfVectorizer(max_features=10000,stop_words='english')

            #Construct the required TF-IDF matrix by fitting and transforming the data
            tfidf_matrix = tfidf.fit_transform(new_df["text"])


            # Compute the cosine similarity matrix
            cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

            data_path = path.abspath(path.join(cosine_sim_data_path))
            logging.info("Training done")
            save(data_path,cosine_sim)
        
        except  Exception as e:
                raise  MovieException(e,sys)
Train_model.train()