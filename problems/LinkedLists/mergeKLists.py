# Merge k Sorted Lists
# Leetcode 23: https://leetcode.com/problems/merge-k-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if lists is None or len(lists) < 1:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.apped(self.mergeTwoLists(l1, l2))
            
            lists = mergedLists
        
        return lists[0]

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
 
        