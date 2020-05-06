# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.best = 1

        def depth(node):
            if not node: return 0
            left, right = depth(node.left), depth(node.right)
            self.best = max(self.best, left+right+1)
            return 1 + max(left, right)
        depth(root)
        return self.best - 1
