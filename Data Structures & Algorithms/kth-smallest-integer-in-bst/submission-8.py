# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        self.cnt = 0
        return self.dfs(root, k)

    
    def dfs(self, root, k):
        if not root:
            return None
        left = self.dfs(root.left, k)
        if left is not None:
            return left
        self.cnt += 1
        if self.cnt == k:
            return root.val
        return self.dfs(root.right, k)
        
        
        

        