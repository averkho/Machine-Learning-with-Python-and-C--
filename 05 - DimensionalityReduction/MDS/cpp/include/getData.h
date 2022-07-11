#include <vector>
#include <string>


struct Data
{
    std::vector <std::string> head;
    std::vector < std::vector <double> > values;
};

Data readCSV(std::string name);

void print(std::vector < std::vector <double> > &v);

void print(std::vector <double> &v);


