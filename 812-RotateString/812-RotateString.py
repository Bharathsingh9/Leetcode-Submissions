# Last updated: 7/3/2026, 12:46:57 PM
class Solution(object):
    def rotateString(self, s, goal):
        return len(s)==len(goal) and goal in (s+s)


