class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_depth_cnt = max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)
        return max_depth_cnt
