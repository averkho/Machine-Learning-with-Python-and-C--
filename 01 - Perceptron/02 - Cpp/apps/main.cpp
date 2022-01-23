#include <iostream>
#include <read_data.h>
#include <string>
#include<vector>


int main(){

    
    dataset train_dat=read_dataset("../data/sentiment_train.tsv");
    dataset test_dat=read_dataset("../data/sentiment_test.tsv");

    std::vector<std::string> stop_words=read_stop_words("../data/stopwords.txt");

    print(stop_words);

    return 0;
}