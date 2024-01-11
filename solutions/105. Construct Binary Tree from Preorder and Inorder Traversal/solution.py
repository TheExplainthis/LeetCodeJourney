from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        tree_map = {num: i for i, num in enumerate(inorder)}
        def construct(left, right):
            if left > right:
                return None
            val = preorder[self.preorder_index]
            mid = tree_map[val]
            self.preorder_index += 1
            node = TreeNode(val)
            node.left = construct(left, mid-1)
            node.right = construct(mid+1, right)
            
            return node

        return construct(0, len(preorder)-1)
