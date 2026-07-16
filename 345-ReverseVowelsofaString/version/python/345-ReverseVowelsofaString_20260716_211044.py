# Last updated: 7/16/2026, 9:10:44 PM
1class Solution:
2    def reverseVowels(self, s: str) -> str:
3        s=list(s)
4        v = "aeiouAEIOU"
5        i,j=0,len(s)-1
6        while i<j:
7            if s[i] in v and s[j] in v:
8                s[i],s[j]=s[j],s[i]
9                i+=1
10                j-=1
11            elif s[i] in v and s[j] not in v:
12                j-=1
13            elif s[i] not in v and s[j] in v:
14                i+=1
15            else:
16                i+=1
17                j-=1
18        return "".join(s)