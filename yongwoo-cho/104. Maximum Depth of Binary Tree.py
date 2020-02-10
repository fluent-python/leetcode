# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        
        def traverse(node, depth):
            if node == None:
                return depth
            else:
                depth += 1
            
            return max(traverse(node.left, depth), traverse(node.right, depth))
        
        return traverse(root, 0)
            
            
            
