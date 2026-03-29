# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # We need two ptrs such that difference of them is n (L-R = n) where R is end of List
        # Also we need dummyNode because we to delete L, we need to link L-1 with L+1
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        
        # right ptr should be n steps ahead of left ptr
        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
        
            

