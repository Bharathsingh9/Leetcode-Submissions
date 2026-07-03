# Last updated: 7/3/2026, 12:46:22 PM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastseen=[-1,-1,-1]
        count=0
        for i in range(0,len(s)):
            lastseen[ord(s[i])-ord('a')]=i
            if min(lastseen)!=-1:
                count+=1+min(lastseen)
        return count