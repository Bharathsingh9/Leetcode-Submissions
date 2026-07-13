# Last updated: 7/13/2026, 9:29:38 PM
1class Solution:
2    def mergeAlternately(self, word1: str, word2: str) -> str:
3        l = ""
4        i=0
5        j=0
6        while i <= len(word1)-1 and j<=len(word2)-1:
7            l+=word1[i]
8            l+=word2[j]
9            i+=1
10            j+=1
11        while i <= len(word1)-1:
12            l+=word1[i]
13            i+=1
14        while j<=len(word2)-1:
15            l+=word2[j]
16            j+=1
17        return l
18
19
20
21
22