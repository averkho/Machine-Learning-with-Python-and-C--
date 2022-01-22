//#include <read_data.h>
#include <iostream>
#include<vector>
#include <string>
#include <fstream>
#include <sstream>



struct dataset{
    std::vector<std::string> texts;
    std::vector<int> labels;
};

void print(dataset &dat){

    size_t n=dat.labels.size();

    for (int i=0; i<n; ++i){

        std::cout << dat.texts[i] << '\t' << dat.labels[i] << std::endl;

    }
}

dataset read_dataset( std::string name){

    std::fstream file(name);

    dataset dat;

    std::string line;
    char delimiter='\t';
    bool read_first_row=false;
    size_t position;

    while (std::getline(file,line)){

        std::string line_value;
        std::stringstream ss(line);

        
        while (std::getline(ss,line_value,delimiter)){
            
            if (read_first_row){

                position=line_value.find_first_of(',');

                dat.labels.push_back(stoi(line_value.substr(0,position)));
                dat.texts.push_back(line_value.substr(position+1));
            }
            read_first_row=true;

        }

    }

    return dat;

};



/*

int main(){

    dataset train_dat=read_dataset("sentiment_train.tsv");
    dataset test_dat=read_dataset("sentiment_test.tsv");

    print(test_dat);

    return 0;
}
*/