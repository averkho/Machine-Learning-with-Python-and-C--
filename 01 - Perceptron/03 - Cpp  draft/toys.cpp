#include <iostream>
#include<string>
#include <vector>
#include <algorithm>
#include <sstream>

int main(){

    //int m=10;
    //int n=20;
    //std::vector<std::vector <int>> A(n, std::vector<int>(m));

    std::string text="My Name is ";

    std::vector<std::string> texts;
    std::string line;

    std::stringstream ss(text);

    

    std::for_each(text.begin(),text.end(),[] (char & c){
        c=::tolower(c);
    });

    //std::cout<< text;

    

    while(std::getline(ss,line,' ')){
        
        texts.push_back(line);

    } 

    

    size_t n=texts.size();
    for (int i=0; i<n; ++i){
        std::cout << texts[i] << "\t";
    }


    return 0;
}