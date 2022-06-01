'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fin=ListNode(0)
        head=fin
        while(list1!=None and list2!=None):
            if(list1.val<list2.val):
                fin.next=ListNode(list1.val)
                list1=list1.next
            else:
                fin.next=ListNode(list2.val)
                list2=list2.next
            fin=fin.next
            
            
        while(list1!=None):
            fin.next=ListNode(list1.val)
            fin=fin.next
            list1=list1.next
            
        while(list2!=None):
            fin.next=ListNode(list2.val)
            fin=fin.next
            list2=list2.next
        return head.next
