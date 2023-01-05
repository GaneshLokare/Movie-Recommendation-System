from movies.exception import MovieException
from movies.logger import logging
import sys
from movies.constants.data_ingestion_constants import movie_id_path

class auto_fetch:
    def __init__(self) -> None:
        pass

    def get_movie_id():
        try:
            f = open(movie_id_path,'r')
            data = f.read()
            data_into_list = data.split(",")
            lst = []
            for i in range(int(data_into_list[-2])+1,int(data_into_list[-2])+101):
                lst.append(i)
            with open(movie_id_path, 'w') as f:
                for num in lst:
                    f.write(f"{num},")
            f.close()
            logging.info("start index {} & end index {} ".format(lst[0],lst[-1]+1))
            return lst[0],lst[-1]
        except  Exception as e:
                raise  MovieException(e,sys)