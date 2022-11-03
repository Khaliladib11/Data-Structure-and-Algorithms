# Merge Two Sorted Lists
# Leetcode 21: https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        if list1 is None and list2 is None:return None
        if list1 is None: return list2
        if list2 is None: return list1

        mergedList = ListNode()
        tail = mergedList

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2
        
        return mergedList.next
