#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

void print(std::vector<std::string> &A){
    size_t n=A.size();

    for(int i=0; i<n; ++i){
        std::cout << A[i] << std::endl;
    }
}

void print(std::map<std::string,int> &D){
    size_t n=D.size();
    for (auto it=D.begin(); it!=D.end(); ++it){
        std::cout << "{ " << (*it).first << " : "<<(*it).second << " }\n";
    }
}

void print(std::vector<std::vector<int>> &a, int n, int m){

    for (int i=0; i<n; ++i){

        for (int j=0; j<m; ++j){
            std::cout << a[i][j] << "\t";
        }
        std::cout << std::endl;
    }

}

std::vector<std::string> extract_words(std::string input_string){

    /*
    Helper function for bag_of_words()
    Inputs a text string
    Returns a list of lowercase words in the string.
    Punctuation and digits are separated out into their own words.
    */
    
    
    size_t n=input_string.size();
    
    for (int i=0; i<n; ++i){

        if ((std::ispunct(input_string[i]) || std::isdigit(input_string[i])) && std::isspace(input_string[i-1]) && std::isspace(input_string[i+1])==false){
            input_string.replace(i+1,0," ");
        } 
        else if ((std::ispunct(input_string[i]) || std::isdigit(input_string[i])) && std::isspace(input_string[i-1])==false && std::isspace(input_string[i+1])){
            input_string.replace(i,0," ");
        }
        else if ((std::ispunct(input_string[i]) || std::isdigit(input_string[i])) && std::isspace(input_string[i-1])==false && std::isspace(input_string[i+1])==false){
            input_string.replace(i,0," ");
            input_string.replace(i+2,0," ");
        }

        if (std::isupper(input_string[i])){
            input_string[i]=std::tolower(input_string[i]);
        }

    }
    

    std::vector<std::string> output_strings;
    std::stringstream ss(input_string);
    std::string word;

    while(std::getline(ss,word,' ')){
       output_strings.push_back(word);
    }

    return output_strings;
    }

std::map<std::string,int> bag_of_words(std::vector<std::string> &texts, std::vector<std::string> &stops, bool remove_stops=true){
    // function to create dictionary of words

    size_t n=texts.size();
    std::string text;
    std::string word;

    std::map<std::string,int> dictionary;

    for (int i=0; i<n; ++i){

        text=texts[i];
        std::vector<std::string> word_list=extract_words(text);
        size_t m=word_list.size();

        for (int j=0; j<m; ++j){

            word=word_list[j];

            if (remove_stops){

                

                if (std::find(stops.begin(),stops.end(),word)==stops.end()){
                    
                    if (dictionary.find(word)==dictionary.end()){
                        dictionary[word]=dictionary.size();
                        
                    }
                }

            } else{

                if (dictionary.find(word)==dictionary.end()){
                        dictionary[word]=dictionary.size();
                }
                
            }
        }

    };

    return dictionary;
}

std::vector<std::vector<int>> make_feature_vector(std::vector<std::string> &texts, std::map<std::string,int> &dictionary){

    int n=texts.size();
    int m=dictionary.size();
    std::vector<std::string> word_list;

    std::vector<std::vector<int>> feature_vector(n,std::vector<int>(m,0));

    //Initiate vector with zeros
    

    for (int i=0; i<n; ++i){

        word_list=extract_words(texts[i]);

        size_t size=word_list.size();

        for (int j=0; j<size; ++j){

            if (dictionary.find(word_list[j])!=dictionary.end()){
                feature_vector[i][dictionary[word_list[j]]]=1;
            }

        }
    }

    


    return feature_vector;
}

int main(){

    std::vector<std::string> texts;
    texts={"A series4 of escap!ades demon",
    "quiet , 2introspective and entert2aining independent"};

    std::vector<std::string> stops;
    stops={"I","you"};

    std::map<std::string,int> dictionary;

    dictionary=bag_of_words(texts,stops);

    std::vector<std::vector<int>> train_features=make_feature_vector(texts,dictionary);

    int n=texts.size();
    int m=dictionary.size();

    print(train_features,n,m); 

    //print(dictionary);
    /*
    for (int i=0; i<texts.size(); ++i){
        std::cout << texts[i] << std::endl;
    }
    */
    return 0;
}