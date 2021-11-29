#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('labeled.csv')
df['comment'] = df['comment'].str.lower()
df[~df.comment.str.contains("http")]


# In[3]:


import re
def tokenizer(text):
    return re.split('[_,][=][-][:][;][*][/][\n][)][(]',text)


# In[4]:


import nltk
nltk.download('stopwords')


# In[5]:


from nltk.corpus import stopwords
stop = stopwords.words('russian')


# In[6]:


X_train = df.loc[:10000, 'comment'].values
y_train = df.loc[:10000, 'toxic'].values
X_test = df.loc[10000:, 'comment'].values
y_test = df.loc[10000:, 'toxic'].values


# In[7]:


from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# In[8]:


tfidf = TfidfVectorizer(strip_accents=None,
                       lowercase=False,
                       preprocessor=None)
param_grid = [{'vect__ngram_range': [(1, 1)],
              'vect__stop_words': [stop, None],
              'vect__tokenizer': [tokenizer],
              'clf__fit_prior':[True, False],
              'clf__alpha': [0.001, 0.01, 0.1, 1.0, 5.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
              'vect__stop_words': [stop, None],
              'vect__use_idf':[False],
              'vect__norm':[None],
              'clf__fit_prior':[True, False],
              'clf__alpha': [0.001, 0.01, 0.1, 1.0, 5.0, 10.0, 100.0]}]


# In[9]:


lr_tfidf = Pipeline([('vect', tfidf),
                    ('clf', MultinomialNB())])
gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                          scoring='accuracy',
                          cv=5, verbose=2,
                          n_jobs=-1)
gs_lr_tfidf.fit(X_train, y_train)


# In[10]:


print('Наилучший набор параметров: %s'
     % gs_lr_tfidf.best_params_)
print('Правильность при перекрестной проверке: %.3f'
     % gs_lr_tfidf.best_score_)
clf = gs_lr_tfidf.best_estimator_
print('Правильность при испытании: %.3f'
     % clf.score(X_test, y_test))



# In[18]:


X = df.loc[:, 'comment'].values
y = df.loc[:, 'toxic'].values
clf.fit(X, y)


# In[40]:


import pickle
import os
s = pickle.dump(clf, open(os.path.join('model.pkl'), 'wb'), protocol=4)

