#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

struct Data
{
    std::vector <std::string> head;
    std::vector < std::vector <double> > values;
};

Data readCSV(std::string name)
{

    std::fstream file(name);
    Data dat;
    std::string line;
    char delimiter{ ',' };
    bool flag{ true };
    while (std::getline(file,line))
    {
        std::string line_value;
        std::stringstream ss(line);

        std::vector <double> v;

        while (std::getline(ss,line_value,delimiter))
        {   
            if (flag)
            {
                dat.head.push_back(line_value);
                
            } 
            else
            {   
                v.push_back(std::stod(line_value));
            }           
        }
        
        flag = false;

        dat.values.push_back(v);
        
    }
    
    return dat;

}

void print(std::vector < std::vector <double> > &v)
{   
    std::cout << v.size() << std::endl;
    for (size_t i = 0; i < v.size(); ++i)
    {
        for (size_t j = 0; j < v[i].size(); ++j)
        {
            std::cout << v[i][j] << std::endl;
        }
        std::cout << std::endl;
    }
}

int main()
{

    Data dat = readCSV("../Data/mds_data.csv");
    std::cout << "Printing " << std::endl;
    print(dat.values);
    return 0;
}