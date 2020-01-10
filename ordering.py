from collections import defaultdict, Counter

def getOccurances(dictionary):

    dict_word_count = defaultdict(int)

    for source, articles in dictionary.items():
        for article in articles:
            for word in article:
                dict_word_count[word[0]] += 1

    return dict_word_count

def getStringArticles(dictionary):

    article_list = []

    for articles in dictionary.values():
        for article in articles:
            article = (article.replace('\n', ''))
            article_list.append(article)
            
    return article_list

def compareArticles(dictionary):
    pass
    # list of articles that are tokenize
    #
    # for each item in the list compare
