# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLinkedList(self, head) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        half = end = head

        prev_half = None
        while end and end.next:
            prev_half = half
            half = half.next
            end = end.next.next

        if prev_half:
            prev_half.next = None
        revHalf = self.reverseLinkedList(half)

        curr = head

        while curr and revHalf:
            nxt = curr.next
            if not nxt:
                curr.next = revHalf
                return
            curr.next = revHalf
            revHalf = revHalf.next
            curr.next.next = nxt
            curr = curr.next.next