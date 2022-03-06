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

void perceptron_step(std::vector<std::vector<double>> &X, std::vector<double> &y,
                                            std::vector<double> current_theta, double current_theta_0=0, bool toy=false){
    /*
    function to implement one step in perceptron algorithm
    */

   

   size_t n=X.size();
   size_t m=X[0].size()

   arma::mat theta(m,1,fill::zeros);

    std::cout << "Matrix " << std::endl;

    std::cout << theta:
   

    }




