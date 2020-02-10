# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
            
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        def check_sum(nums : list, node : TreeNode):
            if node == None:
                return 0
            cnt = 0 
            path_sum = 0
            
            nums.insert(0, node.val)
            for i in nums:
                path_sum += i
                if path_sum == sum:
                    cnt += 1
            
            
            cnt += check_sum(nums.copy(), node.left)
            cnt += check_sum(nums.copy(), node.right)
            
            return cnt
        
 
        
        return check_sum([], root)
                    

