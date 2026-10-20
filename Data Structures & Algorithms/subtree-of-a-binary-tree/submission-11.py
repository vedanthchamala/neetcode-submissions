# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.dfs(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    ## two sub problems. Check every node, and then from every node check if a subtree exists
    def dfs(self, root, sub):
        if not root and not sub:
            return True
        if not root or not sub:
            return False
        if root.val != sub.val:
            return False
        return self.dfs(root.left, sub.left) and self.dfs(root.right, sub.right)



        