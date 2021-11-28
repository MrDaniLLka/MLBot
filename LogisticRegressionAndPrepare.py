#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[8]:


df = pd.read_csv('labeled.csv')


# In[20]:


df[~df.comment.str.contains("http")]


# In[27]:


def tokenizer(text):
    return text.split()


# In[22]:


import nltk
nltk.download('stopwords')


# In[23]:


from nltk.corpus import stopwords
stop = stopwords.words('russian')


# In[29]:


X_train = df.loc[:10000, 'comment'].values
y_train = df.loc[:10000, 'toxic'].values
X_test = df.loc[10000:, 'comment'].values
y_test = df.loc[10000:, 'toxic'].values


# In[31]:


from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(strip_accents=None,
                       lowercase=False,
                       preprocessor=None)
param_grid = [{'vect__ngram_range': [(1, 1)],
              'vect__stop_words': [stop, None],
              'vect__tokenizer': [tokenizer],
              'clf__penalty':['l1', 'l2'],
              'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
              'vect__stop_words': [stop, None],
              'vect__tokenizer': [tokenizer, tokenizer_porter],
              'vect__use_idf':[False],
              'vect__norm':[None],
              'clf__penalty':['l1', 'l2'],
              'clf__C': [1.0, 10.0, 100.0]}]

lr_tfidf = Pipeline([('vect', tfidf),
                    ('clf', LogisticRegression(random_state=0,
                                               solver='liblinear'))])
gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                          scoring='accuracy',
                          cv=5, verbose=2,
                          n_jobs=-1)
gs_lr_tfidf.fit(X_train, y_train)


# In[32]:


print('Наилучший набор параметров: %s'
     % gs_lr_tfidf.best_params_)
print('Правильность при перекрестной проверке: %.3f'
     % gs_lr_tfidf.best_score_)
clf = gs_lr_tfidf.best_estimator_
print('Правильность при испытании: %.3f'
     % clf.score(X_test, y_test))


# In[34]:


clf.predict(['Данич пидаруничкус'])


# In[ ]:




