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
    
    std::vector<std::vector<double>> X;
    std::vector<int> label;
};

void print(dataset &dat){

    size_t n=dat.labels.size();

    for (int i=0; i<n; ++i){

        std::cout << dat.texts[i] << '\t' << dat.labels[i] << std::endl;

    }
}

void print(std::vector<std::vector<double>> &A){

    size_t n=A.size();


}

void print(toy_dataset &dat){
    size_t n=dat.label.size();
    
    for (int i=0; i<n; ++i){
        std::vector<double> x;
        x=dat.X[i];

       size_t  m=x.size();

       for (int j=0; j<m; ++j){
           std::cout << x[j] << '\t';
       }
       std::cout << dat.label[i] << std::endl;
    }
      
}


toy_dataset read_toy_dataset(std::string name, bool read_first_row=false){

    std::fstream file(name);

    toy_dataset dat;

    std::string line;
    char delimiter=',';
    
    while (std::getline(file,line)){ // reading file as a string
        std::string line_value;
        std::stringstream ss(line);

        int count=0;

        std::vector<double> x;
        
        while(std::getline(ss,line_value,delimiter)){
            
            if (read_first_row){
                if (count==0){
                    x.push_back(std::stod(line_value));
                    
                } else if (count==1){
                    x.push_back(std::stod(line_value));
                } else if (count==2){
                    dat.label.push_back(std::stoi(line_value));
                                        
                }else{
                    throw std::logic_error("You have row in a file longer than 2");
                }
            ++count;
                
            }

        }
    if (read_first_row){
         dat.X.push_back(x);
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


