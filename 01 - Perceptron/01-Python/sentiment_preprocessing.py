import pandas as pd
import numpy as np

from string import punctuation,digits

def extract_words(input_string):
    
    """
    Helper function for bag_of_words()
    Inputs a text string
    Returns a list of lowercase words in the string.
    Punctuation and digits are separated out into their own words.
    
    """
    
    for c in punctuation+digits:
        
        input_string=input_string.replace(c,' '+c+' ')
    
    return input_string.lower().split()

def bag_of_words(texts,stops,remove_stops=True):
    
    """
    Inputs a list of string reviews
    Returns a dictionary of unique unigrams occurring over the input

    """
    
    dictionary={}
    for text in texts:
        
        word_list=extract_words(text)
        
        for word in word_list:
            
            if remove_stops:
                
                if word not in stops:
                    
                    if word not in dictionary:
                        
                        dictionary[word]=len(dictionary)           
                
            else:
                
                if word not in dictionary:
                    
                    dictionary[word]=len(dictionary)
    
    return dictionary

def make_feature_vector(texts,dictionary):
    
    """
    Inputs a list of string texts
    Inputs the dictionary of words as given by bag_of_words
    Returns the bag-of-words feature matrix representation of the data.
    The returned matrix is of shape (n, m), where n is the number of texts
    and m the total number of entries in the dictionary.

    """
    
    num_phrases=len(texts)
    feature_matrix=np.zeros([num_phrases,len(dictionary)])
    
    for i,text in enumerate(texts):
        
        word_list=extract_words(text)
        
        for word in word_list:
            
            if word in dictionary:
                
                feature_matrix[i][dictionary[word]]=1
    
    return feature_matrix
    
    
    
    
    
    
    
    
    
    
    
    
    