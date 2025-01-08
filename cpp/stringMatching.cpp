#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
// https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
bool kmp(string a, string b) {
    if (a.size() < b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[0]) continue;
        if (a[i] == b[0]) {
            int k = 0;
            string s;
            for (; k < b.size() && a[i + k] == b[k]; k++) {
                s.push_back(a[i + k]);
            }
            if (s.size() == b.size()) return true;
        }
    }
    return false;
}

template <typename T>
void printVector(const std::vector<T>& vec, const std::string& separator = " ",
    const std::string& prefix = "", const std::string& suffix = "\n") {
    std::cout << prefix;

    for (size_t i = 0; i < vec.size(); ++i) {
        std::cout << vec[i];
        if (i < vec.size() - 1) {
            std::cout << separator;
        }
    }

    std::cout << suffix;
}

class Solution {
public:
    vector<string> stringMatching(vector<string>& words) {
        set<string> temp;
        for (int i = 0; i < words.size(); i++) {
            vector<string> search_space; // this gathers all potential space to search
            for (int j = 0; j < i; j++) search_space.push_back(words[j]);
            for (int j = i + 1; j < words.size(); j++) search_space.push_back(words[j]);
            for (int k = 0; k < search_space.size(); k++)
                if (kmp(search_space[k], words[i]))
                    temp.insert(words[i]);
        }

        vector<string> results(temp.size());
        copy(temp.begin(), temp.end(), results.begin());
        return results;
    }
};
