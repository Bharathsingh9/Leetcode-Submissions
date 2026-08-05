# Last updated: 8/5/2026, 7:12:03 PM
1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        c=sorted(s)
9        g=sorted(t)
10        if "".join(c) in "".join(g) and len(c)==len(g):
11            return True
12        return False
13        