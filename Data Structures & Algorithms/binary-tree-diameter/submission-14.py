# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        through = left + right
        lm = self.diameterOfBinaryTree(root.left)
        rm = self.diameterOfBinaryTree(root.right)
        return max(lm, rm, through)
        

    def maxDepth(self, root):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))







        