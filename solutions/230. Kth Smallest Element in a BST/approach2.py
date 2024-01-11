from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        stack = []
        while len(stack) > 0 or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop(-1)
            res.append(root.val)
            root = root.right
            if len(res) == k: return res[-1]
            