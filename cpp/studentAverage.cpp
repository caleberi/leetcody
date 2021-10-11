/**
 * You are given a two-dimensional matrix that represents the grades of a class of students.
 *  Each grade is represented as an array where the first index is the student’s ID and the
 *  second student is a grade (0 - 100) that the student has received. Given these grades,
 *  calculate the average of each student’s top five scores and return the result.
 *  Note: Each student is guaranteed to have at least 5 scores. Student IDs start from zero and increase by one. Your return variable should be sorted according to student ID.
    Ex: Given the following grades…
    grades = [[1, 100], [1, 50], [2, 100], [2, 93], [1, 39], [2, 87], [1, 89], [1, 87], [1, 90], [2, 100], [2, 76]], return [[1, 83], [2, 91]] 
    (Student one's average is an 83 and student two's average is a 91).
*/

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Student;
vector<vector<int>> studentAverage(vector<vector<int>> &grades);
void printVectors(vector<vector<int>> scores)
{
    for (auto &score : scores)
    {
        cout << "ID :" << score[0] << " , top_score: " << score[1] << " \n";
    }
}

int main()
{
    vector<vector<int>> grades;
    grades.push_back({1, 100});
    grades.push_back({1, 50});
    grades.push_back({2, 100});
    grades.push_back({2, 93});
    grades.push_back({1, 39});
    grades.push_back({2, 87});
    grades.push_back({1, 89});
    grades.push_back({1, 87});
    grades.push_back({1, 90});
    grades.push_back({2, 100});
    grades.push_back({2, 76});
    printVectors(studentAverage(grades));
    return 0;
}

class Student
{
private:
    int id;
    priority_queue<double> scores;
    double laverage_ = 0;

public:
    double average;
    Student() {}
    ~Student() {}
    Student(int id, double score)
    {
        this->id = id;
        addScore(score);
    }
    Student(int id)
    {
        this->id = id;
    }

    void addScore(int score)
    {
        scores.push(score);
    }

    double currentAverage()
    {
        for (int i = 0; i < 5; i++)
        {
            laverage_ += scores.top(); // 0(1)
            scores.pop();              // ?? 0(1) -> 0(NlogN)
        }
        return laverage_ / 5;
    }
};

vector<vector<int>> studentAverage(vector<vector<int>> &grades)
{
    vector<vector<int>> ret = {};
    unordered_map<int, Student> ids;
    for (int i = 0; i < grades.size(); i++)
    {
        if (ids.find(grades[i][0]) == ids.end())
        {
            Student student(grades[i][0], grades[i][1]);
            ids[grades[i][0]] = student;
        }
        else
        {
            ids[grades[i][0]].addScore(grades[i][1]);
        }
    }
    for (auto it = ids.begin(); it != ids.end(); it++)
    {
        ret.push_back({it->first, (int)it->second.currentAverage()});
    }
    return ret;
}
