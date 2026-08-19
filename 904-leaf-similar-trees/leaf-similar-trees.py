# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        ans = []
        def dfs1(root1):
            if not root1:
                return 
            if not root1.left and not root1.right:
                res.append(root1.val)
            dfs1(root1.left)
            dfs1(root1.right)
        dfs1(root1)
        def dfs2(root2):
            if not root2:
                return 
            if not root2.left and not root2.right:
                ans.append(root2.val)
            dfs2(root2.left)
            dfs2(root2.right)
        dfs2(root2)
        return ans == res
