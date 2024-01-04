class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head is not None:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
