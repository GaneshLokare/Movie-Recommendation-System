movie_id_path = "movies/artifacts/data_access/movie_id.txt" # file path for movie id
from movies.data_ingestion.create_id import auto_fetch # get start index movie id and end index movie id for auto fetch
start_index,end_index = auto_fetch.get_movie_id()
movie_data_path = "movies/artifacts/data_access/movies_data.csv"
keywords_data_path = "movies/artifacts/data_access/keywords_data.csv"
credits_data_path = "movies/artifacts/data_access/credits_data.csv"
preprocessed_data_path = "movies/artifacts/data_access/preprocessed_data.csv"
cosine_sim_data_path = "movies/artifacts/data_access/cosine_sim.npy"
