# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = l1
        second = l2
        remainder = 0
        res = ListNode()
        new = res
        while first or second or remainder:
            if first:
                fir = first.val
            else:
                fir = 0
            if second:
                sec = second.val
            else:
                sec = 0
            tot = remainder + fir + sec
            digit = tot % 10 
            remainder = tot // 10
            new.next = ListNode(digit)
            new = new.next
            if first:
                first = first.next
            if second:
                second = second.next
        return res.next
        
        


        