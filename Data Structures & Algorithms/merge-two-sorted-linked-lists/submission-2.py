# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        head = ret = ListNode(-1)
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                ret.next = curr1
                curr1 = curr1.next
            else:
                ret.next = curr2
                curr2 = curr2.next
            ret = ret.next
        if curr1 is None:
            ret.next = curr2
        else:
            ret.next = curr1

        return head.next