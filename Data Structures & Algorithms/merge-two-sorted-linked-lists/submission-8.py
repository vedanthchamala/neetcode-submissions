# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail1 = list1 
        tail2 = list2
        new = ListNode()
        start = new
        while tail1 and tail2:
            if tail1.val <= tail2.val:
                new.next = tail1
                tail1 = tail1.next
            else:
                new.next = tail2
                tail2 = tail2.next
            new = new.next
        if tail1:
            new.next = tail1
        if tail2:
            new.next = tail2
        return start.next


        