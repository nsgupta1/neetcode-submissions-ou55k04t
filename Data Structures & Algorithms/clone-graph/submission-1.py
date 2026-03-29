"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
    1. 
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return node
        headNode = Node(node.val)
        seenNodes = {}
        seenNodes[headNode.val] = headNode
        queue = deque()
        queue.append(node)
        while queue:
            currNode = queue.popleft()
            if currNode.val not in seenNodes:
                newNode = Node(currNode.val) 
                seenNodes[newNode.val] = newNode
            else:
                newNode = seenNodes[currNode.val]
            for nei in currNode.neighbors:
                if nei.val not in seenNodes:
                    neiNode = Node(nei.val)
                    seenNodes[neiNode.val] = neiNode
                    queue.append(nei)
                else:
                    neiNode = seenNodes[nei.val]
                newNode.neighbors.append(neiNode)
        return headNode

                







        
        
        

        