# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Avoid array slices (which cost O(n) each).
        index={val:ind for ind,val in enumerate(inorder)}
        self.pre_ind=0
        def construct(l,r):
            if l>r:
                return None
            root=TreeNode(preorder[self.pre_ind])
            self.pre_ind+=1
            mid=index[root.val]
            root.left=construct(l,mid-1)
            root.right=construct(mid+1,r)
            return root

        return construct(0,len(inorder)-1)
        # if not preorder or not inorder:
        #     return None
        # root=TreeNode(preorder[0])
        # mid=inorder.index(preorder[0])
        # root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        # root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # return root
        