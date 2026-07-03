# Last updated: 7/3/2026, 12:48:18 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        end=len(s)-1
        while s[end]==" ":
            end-=1
        start=end
        while start>=0 and s[start]!=" ":
            start-=1
        return end-start
