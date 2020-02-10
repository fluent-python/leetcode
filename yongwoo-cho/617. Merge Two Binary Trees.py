# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        def traverse(n1, n2):
            if n1 == None and n2 == None:
                return None
            
            if n1 == None:
                l1 = None
                r1 = None
                val1 = 0
            else:
                l1 = n1.left
                r1 = n1.right
                val1 = n1.val
            if n2 == None:
                val2 = 0 
                l2 = None
                r2 = None
            else:
                l2 = n2.left
                r2 = n2.right
                val2 = n2.val
            
            n3 = TreeNode(val1 + val2)
            
            n3.left = traverse(l1, l2)
            n3.right = traverse(r1, r2)
            
            return n3
        
        t3 = traverse(t1,t2)
        return t3
            
            
                
