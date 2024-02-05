import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = [(root, -math.inf, math.inf)]

        while len(stack) > 0:
            curr, lower, upper = stack.pop(-1)
            if curr is None:
                continue
            if curr.val <= lower or curr.val >= upper:
                return False
            stack.append((curr.left, lower, curr.val))
            stack.append((curr.right, curr.val, upper))
        return True
