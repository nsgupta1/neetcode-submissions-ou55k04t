# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, maxVal) -> int:
            if not node:
                return 0
            if node.val >= maxVal:
                maxVal = node.val
                self.res += 1
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
            return self.res
        return dfs(root, root.val)