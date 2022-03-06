#include <armadillo>

// Input matrix of type float

int main(){

  arma::fmat inMat;

// Output matrices
arma::fmat U;
arma::fvec S;
arma::fmat V;

// Perform SVD
arma::svd(U, S, V, inMat);

  return 0;
}
