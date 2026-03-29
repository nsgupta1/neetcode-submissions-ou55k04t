"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
"""
    1. Create a map of seen nodes, old --> new
    2. if you see an existing node, you use it instead of creating a new one
    3. dfs on each node and copy its neighbors by calling same dfs function
    4. return head node
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        oldToNew = {}
        oldToNew[node] = Node(node.val)

        def dfs(root):
            if root not in oldToNew:
                oldToNew[root] = Node(root.val)
            for n in root.neighbors:
                if n not in oldToNew:
                    dfs(n)
                oldToNew[root].neighbors.append(oldToNew[n])
            return
        dfs(node)
        return oldToNew[node]
                

        