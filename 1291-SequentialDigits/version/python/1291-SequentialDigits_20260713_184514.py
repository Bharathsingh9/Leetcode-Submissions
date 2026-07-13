# Last updated: 7/13/2026, 6:45:14 PM
1class Solution:
2    def sequentialDigits(self, low: int, high: int) -> List[int]:
3        ans = []
4
5        s = "123456789"
6        l = str(low)
7        h = str(high)
8
9        for length in range(len(l), len(h) + 1):
10            for start in range(0, 10 - length):
11                num = int(s[start:start + length])
12                if low <= num <= high:
13                    ans.append(num)
14
15        return ans