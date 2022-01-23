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

void print(std::vector<std::string> &A){

    size_t n=A.size();

    for (int i=0; i<n; ++i){
        std::cout << A[i] << std::endl;
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

std::vector<std::string> read_stop_words(std::string file_name, bool read_first=false){

    // reading txt file 

    std::vector<std::string> stop_words;
    std::fstream file(file_name);
    std::string line;
       
    while (std::getline(file,line)){
               
        stop_words.push_back(line);
              
    }
        
    if (read_first){
        return stop_words;
    }
    
    stop_words.erase(stop_words.begin());
    
    return stop_words; 

    
}





int main(){

    bool read_first;

    dataset train_dat=read_dataset("sentiment_train.tsv");
    dataset test_dat=read_dataset("sentiment_test.tsv");

    std::vector <std::string> stop_words;

    stop_words=read_stop_words("stopwords.txt");

    print(stop_words);

    return 0;
}
