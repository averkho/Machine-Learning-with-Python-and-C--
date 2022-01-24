#include <iostream>
#include <read_data.h>
#include <string>
#include<vector>
#include <preprocessing.h>


int main(){

    
    dataset train_dat=read_dataset("../data/sentiment_train.tsv");
    dataset test_dat=read_dataset("../data/sentiment_test.tsv");

    std::vector<std::string> stop_words=read_stop_words("../data/stopwords.txt");
    
    std::map<std::string,int> dictionary;

    dictionary=bag_of_words(train_dat.texts,stop_words);

    print(dictionary);

    return 0;
}