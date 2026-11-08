# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        half = (count + 1) // 2
        find = head
        for _ in range(half - 1):
            find = find.next
        second = find.next
        find.next = None

        rev = second
        prev = None
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        [2, 4, 6]
        [10, 8]

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1 
        



        





        