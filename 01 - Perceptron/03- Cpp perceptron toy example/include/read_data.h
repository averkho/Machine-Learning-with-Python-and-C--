
#include <iostream>
#include<vector>
#include <string>
#include <fstream>
#include <sstream>

struct dataset{
    std::vector<std::string> texts;
    std::vector<int> labels;
};

struct toy_dataset{
    
    std::vector<std::vector<double>> X;
    std::vector<int> label;
};

void print(dataset &dat);

void print(std::vector<std::string> &A);

void print(toy_dataset &dat);

toy_dataset read_toy_dataset(std::string name, bool read_first_row=false);

dataset read_dataset( std::string name);

std::vector<std::string> read_stop_words(std::string file_name, bool read_first=false);

