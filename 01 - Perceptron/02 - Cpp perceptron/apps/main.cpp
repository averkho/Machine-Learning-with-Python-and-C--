#include <iostream>
#include <read_data.h>
#include <string>
#include<vector>
#include <preprocessing.h>
#include <algorithms.h>



int main(){

    
    dataset train_dat=read_dataset("../data/sentiment_train.tsv");
    dataset test_dat=read_dataset("../data/sentiment_test.tsv");

    std::vector<std::string> stop_words=read_stop_words("../data/stopwords.txt");
    
    std::map<std::string,int> dictionary;

    dictionary=bag_of_words(train_dat.texts,stop_words);

    std::vector<std::vector<int>> train_features=make_feature_vector(train_dat.texts,dictionary);
    std::vector<std::vector<int>> test_features=make_feature_vector(test_dat.texts,dictionary);

    int n=test_dat.texts.size();
    int m=dictionary.size();

    //print(dictionary);

    perceptron_step()

    return 0;
}