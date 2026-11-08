# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # [1, 2, 3]
        # [2, 4, 6, 8] 
        # [2, 4, 6, 8, 10]
        # [2, 4, 6, 8, 10, 12]
        #counting the total
        n = 0
        cnt = head
        while cnt:
            n += 1
            cnt = cnt.next
        #half
        mid = (n + 1) // 2 
        cur = head
        #find second half
        for _ in range(mid - 1):
            cur = cur.next
        scnd = cur.next
        cur.next = None    

        #reverse second half
        rev = scnd
        prev = None
        while rev:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        
        #run it up
        [2, 4, 6]
        [10, 8]
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2








        



        
        
        




        