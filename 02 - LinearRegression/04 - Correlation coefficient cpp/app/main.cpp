#include <iostream>
#include <vector>
#include<numeric>
#include<math.h>
#include <read_data.h>

double mean(std::vector<double> &A){

    // Arithmetic mean calculation function

    size_t n=A.size();
    
    return std::accumulate(A.begin(),A.end(),0.0)/n;
};

double correlation(std::vector<double> &X, std::vector<double> &Y){

    //Calculation of correlation coefficient

    size_t n=X.size();

    double x_mean=mean(X);
    double y_mean=mean(Y);

    double numerator=0.0;
    double denumerator_1=0.0;
    double denumerator_2=0.0;

    for (int i=0; i<n; ++i){

        numerator+=(X[i]-x_mean)*(Y[i]-y_mean);
        denumerator_1+=pow((X[i]-x_mean),2);
        denumerator_2+=pow((Y[i]-y_mean),2);
    }

    return numerator/sqrt(denumerator_1*denumerator_2);

};

int main(){

    dataset dat;

    dat=download_data("../data/turbine.csv");

    std::cout << "Correlation coefficient of gas flow and output "<< correlation(dat.gas_flow,dat.mw_output) << std::endl;
    std::cout << "Correlation coefficient of air flow and output "<< correlation(dat.air_flow,dat.mw_output) << std::endl;
    std::cout << "Correlation coefficient of air temperature and output "<< correlation(dat.temperature,dat.mw_output) << std::endl;


    return 0;
}