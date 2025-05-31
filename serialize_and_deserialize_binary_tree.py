# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ar=data.split(',')
        self.i=0
        def dfs():
            if ar[self.i]=="N":
                self.i+=1
                return None
            root = TreeNode(int(ar[self.i]))
            self.i+=1
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
