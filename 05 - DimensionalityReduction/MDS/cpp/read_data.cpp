//#include <read_data.h>
#include <iostream>
#include<vector>
#include <string>
#include <fstream>
#include <sstream>
#include <stdexcept>



struct dataset{
    std::vector<std::string> texts;
    std::vector<int> labels;
};

struct toy_dataset{
    std::vector<double> x1;
    std::vector<double> x2;
    std::vector<int> label;
};

void print(dataset &dat){

    size_t n=dat.labels.size();

    for (int i=0; i<n; ++i){

        std::cout << dat.texts[i] << '\t' << dat.labels[i] << std::endl;

    }
}

void print(toy_dataset &dat){
    size_t n=dat.label.size();
    

    for (int i=0; i<n; ++i){
        std::cout << dat.x1[i] << '\t' << dat.x2[i] << '\t' << dat.label[i] << std::endl;
    }

    
}

void print(std::vector<std::string> &A){

    size_t n=A.size();

    for (int i=0; i<n; ++i){
        std::cout << A[i] << std::endl;
    }

}

toy_dataset read_toy_dataset(std::string name, bool read_first_row=false){

    std::fstream file(name);

    toy_dataset dat;

    std::string line;
    char delimiter=',';
    while (std::getline(file,line)){
        std::string line_value;
        std::stringstream ss(line);

        int count=0;
        
        while(std::getline(ss,line_value,delimiter)){
            
            if (read_first_row){
                if (count==0){
                    dat.x1.push_back(std::stod(line_value));
                    
                } else if (count==1){
                    dat.x2.push_back(std::stod(line_value));
                } else if (count==2){
                    dat.label.push_back(std::stoi(line_value));
                    
                }else{
                    throw std::logic_error("You have row in a file longer than 2");
                }

                
            }
            
            ++count;

        }

        read_first_row=true;

        
    }

    return dat;


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

    
};






int main(){

    bool toy=true;
    bool first_row=false;
    toy_dataset toy_dat=read_toy_dataset("../data/toy.csv",first_row);
    //dataset train_dat=read_dataset("sentiment_train.tsv");
    //dataset test_dat=read_dataset("sentiment_test.tsv");

    //print(test_dat);
    print(toy_dat);
    return 0;
}
