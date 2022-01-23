#include <iostream>
#include <read_data.h>




int main(){

    dataset train_dat=read_dataset("../data/sentiment_train.tsv");
    dataset test_dat=read_dataset("../data/sentiment_test.tsv");

    print(test_dat);

    return 0;
}