from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np


def tokenize(data):
    """ Check if data structure is a dictionary.
    Tokensize the words in each of the titles.
    Extract the Nouns and Verbs and remove stop words
    """

    stop_words = set(stopwords.words('english'))

    if data == dict():
        for source, articles in data.items():
            token_articles = []
            for article in articles:
                    token_article = word_tokenize(article)
                    filtered_article = [w for w in token_article if not w in stop_words]
                    token_articles.append(filtered_article)

            data[source] = token_articles

        return data

    else:
        token_articles = []

        for article in data:
            token_article = word_tokenize(article)
            filtered_article = [w for w in token_article if not w in stop_words]
            token_articles.append(filtered_article)

        return token_articles

def tag_tokens(dictionary):
    """ Compare the returned words.
    If they match with any of them, increment that article by 1 score.
    Order them by the scoring.
    """
    try:
        for source, articles in dictionary.items():
            tagged_tokens = []
            for i in articles:
                i = [v.lower() for v in i]
                i = pos_tag(i)
                tagged_tokens.append(i)

            dictionary[source] = tagged_tokens

        return dictionary

    except ValueError:
        return "Error in data structure. \
        Please see the input data type and ensure that the dictionary is Source : Articles[]. \
        Then ensure that the values are tokenized"

def getNouns(dictionary):
    """ Remove all tokens that are not Nouns and return the dictionary
    """

    try:
        for source, articles in dictionary.items():
            clean_articles = []
            for tokens in articles:
                nouns = []
                for token in tokens:
                    if token[1] == "NN" or token[1] == "NNS" or token[1] == "VBG":
                        nouns.append(token)

                clean_articles.append(nouns)

            dictionary[source] = clean_articles

        return dictionary

    except:
        return "Error, the nouns could not be identified. Check the articles"

def sentenceSimilarities(data):
    
    embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")

    tf.logging.set_verbosity(tf.logging.ERROR)

    with tf.Session() as session:
        session.run([tf.global_variables_initialiser(), tf.tables_initializer()])
        embeddings = session.run(embed(data))

    return np.array(embeddings).tolist()
