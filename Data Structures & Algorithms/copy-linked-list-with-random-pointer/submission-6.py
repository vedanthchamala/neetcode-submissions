"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        #start off by putting the node copy in front of every node
        #then route the random of each copy to the next node of the originals random point
        # and then go through and wire all the copies together
        if not head:
            return None
        cur = head
        while cur:
            copy = Node(cur.val)
            temp = cur.next
            cur.next = copy
            copy.next = temp
            cur = copy.next
        
        new = head.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        return new

        
            

        