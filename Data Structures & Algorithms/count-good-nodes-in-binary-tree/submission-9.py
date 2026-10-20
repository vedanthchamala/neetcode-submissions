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

    #lower nodes MUST be greater than, only make a node the parent if it's greater 

    
    def dfs(self, root, maxVal):
        if not root:
            return 0
        if root.val >= maxVal:
            maxVal = root.val
            self.goodNodes += 1
        self.dfs(root.left, maxVal)
        self.dfs(root.right, maxVal)
        return self.goodNodes
        













        