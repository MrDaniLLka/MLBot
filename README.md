# MLBot
A bot that detects toxic messages from conversation users.
The algorithm is based on the Bayes multinomial classifierThe algorithm is based on the Bayes multinomial classifier.

 1. *BotForVK.py* - script working with vk api. Docs vk-api: https://vk.com/dev/methods and https://vk-api.readthedocs.io/en/latest/index.html#
 1. *Classificator.py* - script that defines spam by Bayesian classification methods. Used libraries:
    - **pandas:** https://pandas.pydata.org/pandas-docs/stable/index.html
    - **nltk:** https://www.nltk.org/
    - **sklearn:** https://scikit-learn.org/stable/index.html
    - **pickle:** https://docs.python.org/3/library/pickle.html
 1. *bad_words.txt* - dataset with toxic words
 1. *good_words.txt* - dataset with neutral words
 1. *labeled.csv* - file for classifier training containing toxic texts
 1. *model.pkl* - file stores the classifier model 
