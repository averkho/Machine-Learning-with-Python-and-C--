#include <iostream>
#include<string>
#include <vector>
#include <algorithm>

int main(){

    std::vector<std::string> a;
    a={"ad","ff","we","gh"};
    
    int n=0;

    if(std::find(a.begin(),a.end(),"f")!=a.end()){
        n=1;
    }

    std::cout << n << std::endl;

    return 0;
}