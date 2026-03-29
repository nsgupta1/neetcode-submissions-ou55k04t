# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        queue = deque()
        queue.append([root, float('-inf'), float('inf')])
        while queue:
            node, l, r = queue.popleft()
            if not (l < node.val < r):
                return False
            if node.left : queue.append([node.left, l, node.val])
            if node.right : queue.append([node.right, node.val, r])
        return True


        