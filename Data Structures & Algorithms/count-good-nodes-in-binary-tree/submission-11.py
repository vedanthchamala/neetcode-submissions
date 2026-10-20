# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.goodNodes = 0
        return self.dfs(root, root.val)

    def dfs(self, root, maxval):
        if not root:
            return 0
        if root.val >= maxval:
            self.goodNodes += 1
            maxval = root.val
        self.dfs(root.left, maxval)
        self.dfs(root.right, maxval)
        return self.goodNodes
        