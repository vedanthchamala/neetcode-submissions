# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.invalid = False
        self.depth(root)
        return False if self.invalid else True
        
    def depth(self, root):
        if not root:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        if abs(left - right) > 1:
            self.invalid = True
        return 1 + max(left, right)

        



        