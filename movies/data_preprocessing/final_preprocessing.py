import pandas as pd
from regex import regex as re
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
lst_stopwords = nltk.corpus.stopwords.words("english")
from movies.constants.data_ingestion_constants import preprocessed_data_path

data = pd.read_csv(preprocessed_data_path,)


data['release_date'] = data['release_date'].apply(lambda x: x[:4])
data['release_date'] = data['release_date'].astype(int)

data['genres'] = data['genres'].apply(lambda x: ' '.join(x))
data['keywords'] = data['keywords'].apply(lambda x: ' '.join(x))
data['production_companies'] = data['production_companies'].apply(lambda x: ' '.join(x))
data['spoken_languages'] = data['spoken_languages'].apply(lambda x: ' '.join(x))
data['spoken_languages'] = data['spoken_languages'].apply(lambda x: ' '.join(x))
data['cast'] = data['cast'].apply(lambda x: ' '.join(x))
data['crew'] = data['crew'].apply(lambda x: ' '.join(x))

data['text'] = data['genres'] + data['keywords'] + data['original_language'] + data['overview'] + data['production_companies'] + data['spoken_languages'] +data['tagline']+ data['cast'] + data['crew']

new_data = data[['id','title','text','popularity','release_date','vote_average']]

# remove all special characters and lower the cases
def remove_special_characters(text):
    text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
    return text

new_data["text"] = new_data["text"].apply(lambda x: remove_special_characters (x))

# remove stpowords
def remove_stopwords(text):
    lst_text = text.split()
    ## remove Stopwords
    if lst_stopwords is not None:
        lst_text = [word for word in lst_text if word not in 
                    lst_stopwords]
    text = " ".join(lst_text)
    return text

new_data["text"] = new_data["text"].apply(lambda x: remove_stopwords (x))

# lemmetization
def lem_words(text):
    lst_text = text.split()
    lem = nltk.stem.wordnet.WordNetLemmatizer()
    lst_text = [lem.lemmatize(word) for word in lst_text]
    text = " ".join(lst_text)
    return text

new_data["text"] = new_data["text"].apply(lambda x: lem_words (x))
print(new_data.head())