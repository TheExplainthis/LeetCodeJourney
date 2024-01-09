import collections
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        buckets = collections.defaultdict(list)

        def dfs(root, layer):
            if root is None:
                return
            buckets[layer].append(root.val)
            dfs(root.left, layer + 1)
            dfs(root.right, layer + 1)
        
        dfs(root, 0)
        return buckets.values()
