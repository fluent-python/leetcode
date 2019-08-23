# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _is_leaf(self, node):
        if (type(node) == int):

            return True
        else:
            return False
        
        
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = [] 
        if root == None:
            return;
   
        if root.left != None:
            if self._is_leaf(root.left):
                output.append(root.left)
            else: 
                output += self.inorderTraversal(root.left)
                
        if root.val != None:
            if self._is_leaf(root.val):
                output.append(root.val)
            else: 
                output += self.inorderTraversal(root.val)
                
                
        if root.right != None:
            if self._is_leaf(root.right):
                output.append(root.right)
            else: 
                output += self.inorderTraversal(root.right)
        
        return output
