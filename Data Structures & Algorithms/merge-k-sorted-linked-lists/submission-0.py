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
        for head in lists:
            if head:
                heapq.heappush(heap, HeapNode(head))
        
        while heap:
            node_wrapper = heapq.heappop(heap)
            currNode = node_wrapper.node
            if currNode.next:
                heapq.heappush(heap, HeapNode(currNode.next))
            res.next = ListNode(currNode.val)
            res = res.next
        return temp.next
