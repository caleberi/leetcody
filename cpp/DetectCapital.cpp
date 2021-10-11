class Solution
{
public:
    bool isAllCap(string word)
    {
        if (word.size() == 1)
        {
            if (isupper(word[0]))
            {
                return true;
            }
            return false;
        }
        bool isUpper = isupper(word[0]);
        for (int i = 1; i < word.length(); i++)
        {
            if (isupper(word[i]))
            {
                isUpper &= true;
            }
            else
            {
                isUpper &= false;
            }
        }
        return isUpper;
    }
    bool isAllSmall(string word)
    {
        if (word.size() == 1)
        {
            if (islower(word[0]))
            {
                return true;
            }
            return false;
        }
        bool iscap = islower(word[0]);
        for (int i = 1; i < word.length(); i++)
        {
            if (islower(word[i]))
            {
                iscap &= true;
            }
            else
            {
                iscap &= false;
            }
        }
        return iscap;
    }
    bool isCapital(string word)
    {
        bool iscap = isupper(word[0]);
        for (int i = 1; i < word.length(); i++)
        {
            if (islower(word[i]))
            {
                iscap &= true;
            }
            else
            {
                iscap &= false;
            }
        }
        return iscap;
    }
    bool detectCapitalUse(string word)
    {
        if (this->isAllSmall(word) && word.size() == 1)
        {
            return true;
        }
        if (this->isAllCap(word) && word.size() == 1)
        {
            return true;
        }

        if (this->isAllSmall(word) && word.size() > 1)
        {
            return true;
        }
        if (this->isAllCap(word) && word.size() > 1)
        {
            return true;
        }
        if (this->isCapital(word) && word.size() > 1)
        {
            return true;
        }
        return false;
    }
};