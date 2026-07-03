# Last updated: 7/3/2026, 12:49:12 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        maxi=0
        g=set()
        for right in range(len(s)):
            while s[right] in g:
                g.remove(s[left])
                left+=1

                
            g.add(s[right])
            maxi=max(maxi,right-left+1)
        return maxi
        