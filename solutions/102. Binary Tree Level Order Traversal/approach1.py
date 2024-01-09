import queue
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
        q = queue.Queue()
        q.put([root, 0])
        while not q.empty():
            node, layer = q.get()
            if not node: continue
            buckets[layer].append(node.val)
            q.put([node.left, layer + 1])
            q.put([node.right, layer + 1])
        return buckets.values()
