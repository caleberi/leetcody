/**
* Definition for singly-linked list.
* struct ListNode {
    * int val
    * ListNode * next
    * ListNode(): val(0), next(nullptr) {}
    * ListNode(int x): val(x), next(nullptr) {}
    * ListNode(int x, ListNode * next): val(x), next(next) {}
    *}
*/
#include <vector>
using namespace std;
class Solution
{
public:
    ListNode *middleNode(ListNode *head)
    {
        vector<ListNode *> store while (head != NULL)
        {
            store.push_back(head)
                head = head->next
        }
        int mid = (store.size()) / 2 return store[mid]
    }
}
