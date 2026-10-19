# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        self.dfs(root)
        return self.best
    
    def dfs(self, root):
        if not root:
            return 0
        self.best = max(self.best, self.dfs(root.left) + self.dfs(root.right))
        return 1 + max(self.dfs(root.left), self.dfs(root.right))

        