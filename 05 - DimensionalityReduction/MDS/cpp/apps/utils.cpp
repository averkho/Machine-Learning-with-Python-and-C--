#include <vector>
#include <string>
#include <random>
#include <ctime>

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

std::vector <std::vector <double> > get_random_uniform(const int n_components, const int n_samples)
{
    std::default_random_engine generator(time(0));
    std::uniform_real_distribution <double> distribution(0.0,1.0);

    std::vector <std::vector <double>> X;
    for (size_t i = 0; i < n_samples; ++i)
    {
        std::vector <double> v;
        for (size_t j = 0; j < n_components; ++j)
        {
            v.push_back(distribution(generator));
        }
        X.push_back(v);
    }
    
    return X;
}