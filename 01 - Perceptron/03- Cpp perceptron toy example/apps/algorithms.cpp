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
                                            perceptron_step_parameters &parameters){
    /*
    function to implement one step in perceptron algorithm
    feature_vector - vector of size 1xn - feature vector of 1 sample
    lablel - the labelof that sample
    */

     
   size_t n=feature_vector.size();
   size_t m=feature_vector.size();

   arma::mat theta_current_arma(m,1);
   arma::mat feature_vector_arma(m,1);

    // converting std::vector to armadillo vector
   for (int i=0; i<m; ++i){
       feature_vector_arma(i,0)=feature_vector[i];
       theta_current_arma(i,0)=parameters.theta[i];
   }
    //std::cout << arma::dot(feature_vector_arma,theta_current_arma) << std::endl;
   // the condition to be checked
   //std::cout << theta_current_arma << std::endl;
   if (label*(parameters.theta_0+arma::dot(feature_vector_arma,theta_current_arma))<=0){
       
       theta_current_arma=theta_current_arma+label*feature_vector_arma;
       parameters.theta_0+=label;
   }

    //converting back armadillo vector to std::vector

    for (int i=0; i<m; ++i){
        parameters.theta[i]=theta_current_arma(i,0);
    }
    
    
   
   return parameters;

    };


   perceptron_step_parameters perceptron(std::vector<std::vector<double>> &X, std::vector<int> &y, 
                                std::vector<int> &iteration_order, int num_rounds){

        /*

        perceptron algorithm realization
        X - matrix of feature vectors
        y - labels
        iteration order - vector of itearation order 
        num_rounds - number of iterations 

        */

        size_t n=y.size();
        size_t m=X[0].size();
        

       //initilize vectors theta and theta 0
    
        std::vector<double> theta={0,0};
        double theta_0=0;

    perceptron_step_parameters parameters;

    parameters.theta=theta;
    parameters.theta_0=theta_0;

    std::vector<double> feature_vector;
    int label;
    
    for (int i=0; i<num_rounds; ++i){

        for (int j=0; j<n; ++j){
            
            feature_vector=X[iteration_order[j]];
            
            label=y[iteration_order[j]];

            parameters=perceptron_step(feature_vector,label,parameters);

        }
   
    }

return parameters;

   } 




