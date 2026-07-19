# Last updated: 7/19/2026, 12:25:27 PM
1class Solution:
2    def smallestSubsequence(self, s: str) -> str:
3        last = {c: i for i, c in enumerate(s)}
4        stack = []
5        seen = set()
6
7        for i, c in enumerate(s):
8            if c in seen:
9                continue
10
11            while stack and c < stack[-1] and last[stack[-1]] > i:
12                seen.remove(stack.pop())
13
14            stack.append(c)
15            seen.add(c)
16
17        return "".join(stack)