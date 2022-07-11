#include <vector>
#include <string>

struct Xy{
    std::vector <std::vector <double> > X;
    std::vector <int> y;
};

Xy getX(std::vector <std::vector <double> > &v, std::vector <std::string> &head, std::string yName = "y")
{
    Xy df;
    
    int count{ 0 };
    for (size_t i = 0; i < head.size(); ++i)
    {
        if (head[i] == "y")
        {
            break;
        }
        else
        {
            ++count;
        }
    }
    
    for (size_t i = 0; i < v.size(); ++i)
    {
        std::vector <double> v1;
        for (size_t j = 0; j < v[i].size(); ++j)
        {   
            if (j < count)
            {   
                
                v1.push_back(v[i][j]);
            }
            else if (j == count)
            {
                df.y.push_back(int(v[i][j]));
            }
                        
        }

        df.X.push_back(v1);
        
    }

    return df;

}