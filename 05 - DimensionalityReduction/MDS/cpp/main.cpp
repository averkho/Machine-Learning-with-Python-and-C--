#include <iostream>
#include <string>
#include <cmath>
#include <stdexcept>

#include <getData.h>
#include <math.h>
#include <utils.h>

struct smacof_output{
    std::vector <double> pos;
    double stress;
    int n_init;
};

std::vector <std::vector <double> > upper_triangle(int n_samples)
{   
    // function to create upper triangle matrix filled with 1, having size (n_samples x n_samples)
    std::vector <std::vector <double> > sim_flat;
    int count { 0 };

    for (int i = 0; i < n_samples; ++i)
    {
        std::vector <double> v;

        for (int j = 0; j < n_samples; ++j)
        {
            if (j >= count)
            {
                v.push_back(1);
            }
            else
            {
                v.push_back(0);
            }
        }
        ++count;
        sim_flat.push_back(v);
    }

    return sim_flat;
}

bool check_for_elementwise_multiplication(
    std::vector <std::vector <double> > &v1,
    std::vector <std::vector <double> > &v2
)
{
    if (v1.size() == v2.size() && v1[0].size() == v2[0].size())
    {
        return true;
    }
    else
    {
        return false;
    }
}

std::vector <std::vector <double> > element_wise_multiplication (
    std::vector <std::vector <double> > &v1,
    std::vector <std::vector <double> > &v2
)
{
    if (check_for_elementwise_multiplication(v1,v2) == false)
    {
        throw std::invalid_argument("Inconsistent size of matrixes");
    }
    
    size_t n = v1.size();
    size_t m = v1[0].size();
    std::vector < std::vector <double> > sim_flat;

    for (size_t i = 0; i < n; ++i)
    {   
        std::vector <double> v;

        for (size_t j = 0; j < m; ++j)
        {
            v.push_back(v1[i][j] * v2[i][j]);
        }

        sim_flat.push_back(v);
    }

    return sim_flat;
}


void single_smacof (std::vector <std::vector <double> > dissimilarities,
                            bool metric = true,
                            int n_components = 2,
                            int init = -1,
                            int max_iter = 300,
                            int verbose = 0,
                            double eps = 0.001,
                            int random_state = 0)
    {
        int n_samples = dissimilarities.size();
        std::vector <std::vector <double> > sim_flat = upper_triangle(n_samples);
        sim_flat = element_wise_multiplication(sim_flat,dissimilarities);
        std::vector <double> sim_flat_w;
        
        for (size_t i = 0; i < n_samples; ++i)
        {
            for (size_t j = 0; j < n_samples; ++j)
            {   
                if (sim_flat[i][j] != 0)
                {
                    sim_flat_w.push_back(sim_flat[i][j]);
                }
            }
        }
        
    

    }

void smacof(
            std::vector <std::vector <double> > &dissimilarity_matrix_,
            bool metric = true,
            int n_components = 2,
            int init = 1,
            int n_init = 8,
            int n_jobs = 1,
            int max_iter = 300,
            int verbose = 0,
            double eps = 0.001,
            int random_state = -1,
            bool return_n_iter = true
        )
    {
        smacof_output output;
        
        if (n_jobs == 1)
        {   std::cout << "Debug #3" << std::endl;
            for (int it = 0; it < n_init; ++it)
            {
                std::cout << "I am here " << std::endl;
                single_smacof(dissimilarity_matrix_, metric, n_components, init, max_iter, 
                                        verbose, eps,  random_state);
                    
            
            }
        }

    }



class MDS
{
    public:
    int n_components;
    bool metric;
    int n_init;
    int max_iter;
    int verbose;
    double eps;
    int n_jobs;
    int random_state;
    std::string dissimilarity;

    std::vector <std::vector <double> > dissimilarity_matrix_;

    MDS(int _n_components = 2, bool _metric = true, int _n_init = 4, int _max_iter = 300, int _verbose = 0,
        double _eps = 0.001,int _n_jobs = 1, int _random_state = -1, std::string _dissimilarity = "euclidean")
    {

        n_components = _n_components;
        metric = _metric;
        n_init = _n_init;
        max_iter = _max_iter;
        verbose = _verbose;
        eps = _eps;
        n_jobs = _n_jobs;
        random_state = _random_state;
        dissimilarity = _dissimilarity;
    }

    public:

    std::vector <std::vector <double> > fitTransform(std::vector <std::vector <double> > X, int init = -1)
    {
        if (dissimilarity == "euclidean")
        {
            this -> dissimilarity_matrix_ = euclidianDistances(X);
                        
        }

        bool return_n_iter;
        std::cout << "Debug #1" << std::endl;
        smacof(
            dissimilarity_matrix_,
            metric = this -> metric,
            n_components = this -> n_components,
            init = init,
            n_init = this -> n_init,
            n_jobs = this -> n_jobs,
            max_iter = this -> max_iter,
            verbose = this -> verbose,
            eps = this -> eps,
            random_state = this -> random_state,
            return_n_iter = true
        );
        

        
        return this -> dissimilarity_matrix_;
    }

    void show()
    {
        std::cout << "Print " << std::endl;
    }

};



int main(){

    Data dat = readCSV("../Data/mds_data.csv");
    std::cout << "Printing " << std::endl;
    
    MDS* mds_scaling = new MDS();
    Xy df = getX(dat.values, dat.head);
    std::vector <std::vector <double> > T = mds_scaling -> fitTransform(df.X);
    std::cout << "Printing matrix T " << std::endl;
    
        

    return 0;

}