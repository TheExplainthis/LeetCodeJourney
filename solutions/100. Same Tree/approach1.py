from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack, q_stack = [p], [q]

        while p_stack and q_stack:
            p_curr = p_stack.pop()
            q_curr = q_stack.pop()

            if p_curr and q_curr:
                if p_curr.val != q_curr.val:
                    return False
                p_stack.extend([p_curr.right, p_curr.left])
                q_stack.extend([q_curr.right, q_curr.left])
            elif p_curr or q_curr:
                return False

        return len(p_stack) == len(q_stack)
