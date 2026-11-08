# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        cnt = head
        while cnt:
            count += 1
            cnt = cnt.next
        remove = count - n
        if remove == 0:
            return head.next
        before = head
        for _ in range(remove - 1):
            before = before.next
        before.next = before.next.next
        return head
