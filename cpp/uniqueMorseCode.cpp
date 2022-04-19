#include <vector>
#include <unordered_map>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>

using namespace std;

class Solution {
public:
    unordered_map<char,string> code_table;
    void fillMorseCodeTable(){
        vector<string> rep = {
            ".-","-...","-.-.","-..",
            ".","..-.","--.","....",
            "..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."
        };
         
        int i = 97;
        for (string s : rep){
            char letter = static_cast<char>(i);
            if(code_table.find(letter)==code_table.end()){
                code_table[letter] = s;
                i++;
            }
        }
    }
    int uniqueMorseRepresentations(vector<string>& words) {
        fillMorseCodeTable();
        set<string> transformation;
        for_each(words.begin(),words.end(),[&transformation](string word){
            stringstream ss;
            for (int i = 0; i < word.size(); i++)
                ss << code_table[word[i]];
            transformation.insert(ss.str());
        });
        return transformation.size();
    }
};