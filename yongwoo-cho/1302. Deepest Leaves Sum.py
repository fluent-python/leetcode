# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        level = 0 
        level_sum = {}
        
        
        def checkLevel(node, level):
            if node == None:
                return;
            checkLevel(node.left, level+1)
            checkLevel(node.right, level+1)
            
            if level in level_sum.keys():
                level_sum[level] += node.val
            else:
                level_sum[level] = node.val
        
        checkLevel(root, level)
        print(level_sum)
        key_sorted = sorted(level_sum, reverse=True)
        
        
        return level_sum[key_sorted[0]]
        
         
