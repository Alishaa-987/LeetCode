# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ct=0
        maxi=root.val
        def countgoodu(rt,maxi):
            nonlocal ct
            if(not rt):
                return
            if(rt.val>=maxi):
                maxi=rt.val
                ct+=1
            countgoodu(rt.left,maxi)
            countgoodu(rt.right,maxi)

        countgoodu(root,maxi)
        return ct