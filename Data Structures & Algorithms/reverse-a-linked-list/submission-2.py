# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currHead = None
        curr = head
        while curr != None:
            n = curr.next
            curr.next = currHead
            currHead = curr
            curr = n
        
        return currHead