#include <vector>
#include <string>

struct Xy{
    std::vector <std::vector <double> > X;
    std::vector <int> y;
};

Xy getX(std::vector <std::vector <double> > &v, std::vector <std::string> &head, std::string yName = "y");