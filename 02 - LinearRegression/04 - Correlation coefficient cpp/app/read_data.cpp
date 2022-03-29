#include<iostream>
#include<vector>
#include<fstream>
#include<sstream>
#include <string>

struct dataset{

    std::vector<double> gas_flow;
    std::vector<double> air_flow;
    std::vector<double> mw_output;
    std::vector<double> temperature;

};

dataset download_data(std::string name){

    std::fstream file(name);

    dataset dat;

    std::string line;
    char delimiter=',';
    bool first_row=false;

    while (std::getline(file,line)){
        std::string line_value;
        std::stringstream ss(line);

        if (first_row){

            int count=0;
            while(std::getline(ss,line_value,delimiter)){
                ++count;

                if (count==3){
                    dat.gas_flow.push_back(std::stod(line_value));
                } else if (count==4){
                    dat.air_flow.push_back(std::stod(line_value));
                } else if (count==5){
                    dat.mw_output.push_back(std::stod(line_value));
                } else if (count==6){
                    dat.temperature.push_back(std::stod(line_value));
                }

            }

            
        }
    first_row=true;
    }

    return dat;

}

void print(std::string name, std::vector<double> &A){

    size_t n;
    n=A.size();
    std::cout << "I am printing vector of " << name << "  " << std::endl;

    for (int i=0; i<n; ++i){
        std::cout << A[i] << '\t';
    }
}

/*
int main(){

    dataset dat;

    dat=read_data("./data/turbine.csv");
    print("Gas flow",dat.gas_flow);
    print("MW output",dat.mw_output);

    return 0;
}
*/