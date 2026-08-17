# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = []
        ans = []
        def preorder(p):
            if not p:
                res.append(None)
                return
            res.append(p.val)
            preorder(p.left)
            preorder(p.right)
        preorder(p)
        def preorder1(q):
            if not q:
                ans.append(None)
                return
            ans.append(q.val)
            preorder1(q.left)
            preorder1(q.right)
        preorder1(q)
        return res == ans

