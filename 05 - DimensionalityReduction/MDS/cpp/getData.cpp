#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

struct Data
{
    std::vector <std::string> head;
    std::vector <float> values;
};

void readCSV(std::string name)
{

    std::fstream file(name);
    Data dat;
    std::string line;
    char delimiter{ ',' };
    std::cout << "Debug #1" << std::endl;
    while (std::getline(file,line))
    {
        std::string line_value;
        std::stringstream ss(line);

        while (std::getline(ss,line_value,delimiter))
        {
            std::cout << line_value << std::endl;
        }
    }

}

int main()
{

    readCSV("../Data/mds_data.csv");
    return 0;
}