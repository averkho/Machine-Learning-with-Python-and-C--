#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>
#include <algorithm>

void print(std::vector<std::string> &A);

void print(std::map<std::string,int> &D);

std::vector<std::string> extract_words(std::string input_string);

std::map<std::string,int> bag_of_words(std::vector<std::string> &texts, std::vector<std::string> &stops, bool remove_stops=true);