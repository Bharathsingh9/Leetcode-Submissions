# Last updated: 7/3/2026, 12:46:09 PM
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxi=0
        level=0
        for i in range(len(s)):
            if s[i]=="(":
                level+=1
                maxi=max(maxi,level)
            elif s[i]==")":
                level-=1
        return maxi

        