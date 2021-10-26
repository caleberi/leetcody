#include <stdlib.h>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include  <iostream>
#include <string>

int main() {
    int N;
    std::vector<std::string> data;
    std::cin >> N;
    std::string word;
    while (std::cin>>word)
        data.push_back(word);
    int  i = 0;
    std::unordered_map<std::string,int> freq;
    for (;i < N; i++)
        std::sort(data[i].begin(),data[i].end());
    i=0;
    for (; i < N; i++)
    {
        if(freq.find(data[i])==freq.end())
            freq[data[i]] = 1;
        else
            freq[data[i]]++;
    }
    std::pair<std::string,int> answer = {"",-1};
    for(auto d:freq){
        if(d.second>=answer.second){
            answer=d;
        }
    }
    std::cout << answer.second << std::endl;
}