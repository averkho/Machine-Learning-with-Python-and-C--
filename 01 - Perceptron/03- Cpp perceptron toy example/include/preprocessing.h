#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

void print(std::vector<std::string> &A);

void print(std::map<std::string,int> &D);

void print(std::vector<std::vector<int>> &a, int n, int m);

std::vector<std::string> extract_words(std::string input_string);

std::map<std::string,int> bag_of_words(std::vector<std::string> &texts, std::vector<std::string> &stops, bool remove_stops=true);

std::vector<std::vector<int>> make_feature_vector(std::vector<std::string> &texts, std::map<std::string,int> &dictionary);