
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

dataset read_dataset( std::string name);

