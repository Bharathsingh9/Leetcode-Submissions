# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue  = deque([root])
        res = []
        while queue:
            l = []
            size = len(queue)
            for i in range(size):
                n = queue.popleft()
                l.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            res.append(l)
        ans = []
        for i in range(len(res)):
            ans.append(res[i][-1])
        return ans
                