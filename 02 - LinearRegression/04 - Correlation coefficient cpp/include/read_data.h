#include <iostream>
#include <vector>
#include<fstream>
#include<sstream>
#include<string>

struct dataset{

    std::vector<double> gas_flow;
    std::vector<double> air_flow;
    std::vector<double> mw_output;
    std::vector<double> temperature;

};

dataset download_data(std::string name);

void print(std::string name, std::vector<double> &A);

