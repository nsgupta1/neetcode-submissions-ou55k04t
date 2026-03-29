# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        carry = 0
        while l1 or l2:
            t1 = l1.val if l1 else 0
            t2 = l2.val if l2 else 0
            total = t1 + t2 + carry
            carry = total // 10
            res.next = ListNode(total%10)
            res = res.next
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
        if carry > 0:
            res.next = ListNode(carry)
        return dummy.next

