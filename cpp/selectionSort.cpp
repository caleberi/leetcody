#include <vector>
using namespace std;

vector<int> selectionSort(vector<int> array)
{
    for (int i = 0; i < array.size() - 1; i++)
    {
        int selected = i;
        for (int j = i + 1; j < array.size(); j++)
        {
            if (array[selected] > array[j])
            {
                selected = j;
            }
        }
        swap(array[i], array[selected]);
    }
    return array;
}
