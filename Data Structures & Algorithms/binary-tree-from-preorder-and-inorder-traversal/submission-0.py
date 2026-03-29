# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        store = {val: idx for idx, val in enumerate(inorder)}
        idx = 0

        def dfs(l, r):
            nonlocal store
            nonlocal idx
            if l > r:
                return None
            val = preorder[idx]
            root = TreeNode(val)
            idx += 1
            mid = store.get(val)
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        
        return dfs(0, len(inorder)-1)