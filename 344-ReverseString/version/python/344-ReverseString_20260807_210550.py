# Last updated: 8/7/2026, 9:05:50 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        i = 0
4        j = len(s)-1
5        while i<=j:
6            s[i],s[j]=s[j],s[i]
7            i+=1
8            j-=1
9        return s
10        