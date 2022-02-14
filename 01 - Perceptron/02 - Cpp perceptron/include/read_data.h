
#include <iostream>
#include<vector>
#include <string>
#include <fstream>
#include <sstream>

struct dataset{
    std::vector<std::string> texts;
    std::vector<int> labels;
};

void print(dataset &dat);

void print(std::vector<std::string> &A);

dataset read_dataset( std::string name);

std::vector<std::string> read_stop_words(std::string file_name, bool read_first=false);

