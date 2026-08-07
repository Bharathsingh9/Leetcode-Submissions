# Last updated: 8/7/2026, 9:28:03 PM
1class Solution:
2    def findTheDifference(self, s: str, t: str) -> str:
3        r = 0
4        for i in s + t:
5            r ^= ord(i)
6        return chr(r)