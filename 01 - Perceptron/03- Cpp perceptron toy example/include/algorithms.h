#include <iostream>
#include <vector>
#include <string>
#include <armadillo>

struct toy_parameters{

    std::vector<std::vector<double>> theta;
    std::vector<double> theta_0;
    
};

struct perceptron_step_parameters{

    std::vector<double> theta; // theta vector of size n - number of features
    double theta_0;
};




perceptron_step_parameters perceptron_step(std::vector<double> &feature_vector, int label, 
                                            perceptron_step_parameters &parameters);

perceptron_step_parameters perceptron(std::vector<std::vector<double>> &X, std::vector<int> &y, 
                                std::vector<int> &iteration_order, int num_rounds);