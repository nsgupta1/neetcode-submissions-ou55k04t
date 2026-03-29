# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            return
        
        dfs(root)
        prev = arr[0]
        for i in range(1, len(arr)):
            if prev >= arr[i]:
                return False
            prev = arr[i]
        return True
        