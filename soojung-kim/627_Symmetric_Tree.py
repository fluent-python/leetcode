# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.check(root.left, root.right)

    def check(self, lnode, rnode):
        if lnode and rnode:
            f1 = lnode.val == rnode.val
            f2 = self.check(lnode.left, rnode.right)
            f3 = self.check(lnode.right, rnode.left)
            return f1 and f2 and f3
        return (not lnode) and (not rnode)