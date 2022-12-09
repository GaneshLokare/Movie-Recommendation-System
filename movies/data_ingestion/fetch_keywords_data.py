import pandas as pd
import requests
import os.path as path
from pandas.io.json import json_normalize
from pandas import json_normalize
import sys

from movies.exception import MovieException
from movies.logger import logging
from movies.constants.data_ingestion_constants import start_index, end_index ,keywords_data_path


class keywords_data:
    def __init__():
        pass

    def fetch_data():
        try:

            df = pd.DataFrame()

            for i in range(start_index,end_index):
                res = requests.get('https://api.themoviedb.org/3/movie/{}/keywords?api_key=8265bd1679663a7ea12ac168da84d2e8'.format(i))
                array = res.json()
                temp_df = json_normalize(array)
                df = pd.concat([df,temp_df],ignore_index=True)


            df1 = df[['id','keywords']]

            new_df = df1.dropna()

            keywords_path = path.abspath(path.join(keywords_data_path))
            logging.info("Fetching movies data done")
            logging.info("{} data points are fetched".format((end_index-start_index)))
            return new_df.to_csv(keywords_path,index=False)

            

        except  Exception as e:
                raise  MovieException(e,sys)

keywords_data.fetch_data()