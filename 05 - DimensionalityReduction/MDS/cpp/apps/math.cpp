#include <iostream>
#include <vector>
#include <cmath>



double distance(std::vector <double> &x1, std::vector <double> &x2)
{
    double sum{ 0 };

    if (x1.size() != x2.size())
    {
        throw std::invalid_argument("vector x1 and x2 must be of the same size");
    }

    for (size_t i = 0; i < x1.size(); ++i)
    {
        sum += pow(x2[i] - x1[i],2);
    }

    sum = sqrt(sum);
    
    return sum;
}

std::vector <std::vector <double> > euclidianDistances(std::vector <std::vector <double> > &X)
{
    size_t rows = X.size();
    size_t columns = X[0].size();
    std::vector <std::vector <double> > dissimilarity_matrix;
    
    for (size_t i = 0; i < rows; ++i)
    {   
        std::vector <double> x1;
        x1 = X[i];
        std::vector <double> v;
        for (size_t j = 0; j < rows; ++j)
        {   
            std::vector <double> x2;
            x2 = X[j];
            
            v.push_back(distance(x1,x2));
        }

        dissimilarity_matrix.push_back(v);
    }

return dissimilarity_matrix;

}