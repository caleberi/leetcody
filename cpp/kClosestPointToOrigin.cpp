#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;

class Solution
{
public:
    long manhattanDistance(int x1, int x2, int y1, int y2)
    {

        long x = x2 * x2;
        long y = y2 * y2;
        return x + y;
    }

    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        vector<pair<vector<int>, long>> costDistanceForPoints;
        for (int i = 0; i < points.size(); i++)
        {
            pair<vector<int>, long> t = {points[i], manhattanDistance(0, points[i][0], 0, points[i][1])};
            costDistanceForPoints.push_back(t);
        }

        sort(
            costDistanceForPoints.begin(),
            costDistanceForPoints.end(),
            [](const pair<vector<int>, long> &a, const pair<vector<int>, long> &b) -> bool
            { return a.second > b.second ? true : false; });

        vector<vector<int>> ret;
        int start = costDistanceForPoints.size() - k;
        for (; start < costDistanceForPoints.size(); start++)
            ret.push_back(costDistanceForPoints[start].first);

        return ret;
    }
};
