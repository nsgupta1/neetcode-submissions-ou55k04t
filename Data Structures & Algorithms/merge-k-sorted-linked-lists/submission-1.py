# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class HeapNode:
    def __init__(self, node:ListNode):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        temp = ListNode()
        res = temp
        counter = 0
        for head in lists:
            if head:
                counter += 1
                heapq.heappush(heap, (head.val, counter, head))
        
        while heap:
            val, cnt, currNode = heapq.heappop(heap)
            if currNode.next:
                counter += 1
                heapq.heappush(heap, (currNode.next.val, counter, currNode.next))
            res.next = ListNode(currNode.val)
            res = res.next

        return temp.next
