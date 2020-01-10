from irish_sites import irishTimesScrape, irishIndependantScrape, RTEScrape, journalScrape
from word_parsing import tokenize, tag_tokens, getNouns
from ordering import getOccurances, getStringArticles, compareArticles

def irishSites():
    top_headlines = dict()
    top_headlines = irishTimesScrape(top_headlines)
    top_headlines = irishIndependantScrape(top_headlines)
    top_headlines = RTEScrape(top_headlines)
    top_headlines = journalScrape(top_headlines)

    string_articles = getStringArticles(top_headlines)
    print(string_articles)
    sentence_similarities = sentenceSimilarities(string_articles)
    print(sentence_similarities)
    # tokenize_top_headlines = tokenize(string_articles) # Also removes stopwords
    # print(tokenize_top_headlines)

    # TRY TO ANALYSE EACH OF THE STRINGS - BUILD FUNCTION
    # DO SEMANTIC ANALYSIS ON THIS


    # tagged_tokens = tag_tokens(tokenize_top_headlines)
    # nouns = getNouns(tagged_tokens)
    # print(articles)




irishSites()


# Articles:
# https://towardsdatascience.com/basic-binary-sentiment-analysis-using-nltk-c94ba17ae386


# Send the stuff to Ankit
# Rank the articles based on occruances
#
