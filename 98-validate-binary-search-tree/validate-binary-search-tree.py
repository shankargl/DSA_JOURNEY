# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        def tra(root):
            if root is None:
                return
            tra(root.left)
            ans.append(root.val)
            tra(root.right)
        tra(root)
        now=sorted(ans)
        if len(set(ans))!=len(ans):
            return False
        return ans==now