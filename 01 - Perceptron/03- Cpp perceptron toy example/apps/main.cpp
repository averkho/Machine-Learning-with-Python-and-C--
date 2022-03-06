#include <iostream>
#include <read_data.h>
#include <string>
#include <vector>
#include <preprocessing.h>
#include <algorithms.h>
#include <algorithm>
#include <ctime>



int main(){

    bool first_row=false;

    toy_dataset dat=read_toy_dataset("./data/toy.csv",first_row);

    size_t n=dat.label.size();

    std::cout << "Enter number of rounds ";
    
    int num_rounds;

    std::cin >> num_rounds;

    std::vector<int> iteration_order;
    std::srand(unsigned(std::time(0)));

    for (int i=0; i<n; ++i){
        iteration_order.push_back(i);
    }

    std::random_shuffle(iteration_order.begin(),iteration_order.end());

    perceptron_step_parameters parameters=perceptron(dat.X, dat.label, iteration_order, num_rounds);
    
    std::cout << parameters.theta_0 << std::endl;
    std::cout << parameters.theta[0] << std::endl;

    
    
    return 0;
}