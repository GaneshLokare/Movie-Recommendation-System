import pandas as pd
from movies.constants.data_ingestion_constants import preprocessed_data_path
data = pd.read_csv("movies/artifacts\data_access\preprocessed_data.csv")
print(data)