class Solution {
public:
        void reverse(vector<char> &s, int left, int right)
{
        if (left >= right)
                return;
        swap(s[left], s[right]);
        reverse(s, left + 1, right - 1);
        }
    void reverseString(vector<char>& s) {
        return reverse(s,0,s.size()-1);
    }
};