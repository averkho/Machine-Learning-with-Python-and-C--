import pandas as pd
import numpy as np

import sentiment_preprocessing as preprocessing
import sentiment_algorithms as algorithms
 

import os

files=os.listdir('./')
print(files)


train_dat=pd.read_csv('./sentiment_train.tsv')
test_dat=pd.read_csv('./sentiment_test.tsv')

stop_words=pd.read_csv('./stopwords.txt',delimiter='\t')
stop_words.columns=['stops']
stop_words=list(stop_words['stops'])

dictionary=preprocessing.bag_of_words(list(train_dat['Phrase']),stop_words)

train_features=preprocessing.make_feature_vector(list(train_dat['Phrase']),dictionary)
test_features=preprocessing.make_feature_vector(list(test_dat['Phrase']),dictionary)

train_labels=np.array(train_dat['Sentiment'])
test_labels=np.array(test_dat['Sentiment'])


theta,theta_0=algorithms.perceptron(train_features,train_labels,num_iterations=10)