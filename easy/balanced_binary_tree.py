# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) != -1
            
            
    def dfs(self,root):
        if root == None:
            return True
        
        left_height = self.dfs(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.dfs(root.right)
        if right_height == -1:
            return -1
        
        return 1+max(left_height,right_height) if abs(left_height-right_height)<=1 else -1