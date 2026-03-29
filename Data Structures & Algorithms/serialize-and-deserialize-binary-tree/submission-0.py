# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = ""
        def dfs(root):
            nonlocal res
            if not root:
                res += ",N"
                return
            if res:
                res += "," + str(root.val)
            else:
                res += str(root.val)
            dfs(root.left)
            dfs(root.right)
            return
        dfs(root)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        arr = data.split(",")
        i = 0
        
        def dfs() -> Optional[TreeNode]:
            nonlocal i
            if i >= len(arr) or arr[i] == "N":
                i += 1
                return None
            root = TreeNode(arr[i])
            i += 1
            root.left = dfs()
            root.right = dfs() 
            return root

        return dfs()