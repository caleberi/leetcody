#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <cmath>
#include <vector>

using namespace std;
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/?envType=daily-question&envId=2025-01-01
class Solution {
public:
    int maxScore(string s) {
        vector<int> prefix_zeros(s.size()); // 0(1)
        fill(prefix_zeros.begin(), prefix_zeros.end(), 0);
        vector<int> prefix_ones(s.size());  // 0(1)
        fill(prefix_ones.begin(), prefix_ones.end(), 0);
        int zero = 0, ones = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] != '0') { if (i - 1 >= 0) prefix_zeros[i] = prefix_zeros[i - 1]; }
            else { zero++; prefix_zeros[i] = zero; }
        }
        for (int i = s.size() - 1; i > 0; i--) {
            if (s[i] != '1') { if (i + 1 < s.size()) prefix_ones[i] = prefix_ones[i + 1]; }
            else { ones++; prefix_ones[i] = ones; }
        }
        int answer = INT_MIN;
        for (int i = 1; i < s.size(); i++)
            answer = (answer > prefix_ones[i] + prefix_zeros[i - 1]) ? answer : (prefix_ones[i] + prefix_zeros[i - 1]);
        return answer;
    }
};