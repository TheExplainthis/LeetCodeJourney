class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
