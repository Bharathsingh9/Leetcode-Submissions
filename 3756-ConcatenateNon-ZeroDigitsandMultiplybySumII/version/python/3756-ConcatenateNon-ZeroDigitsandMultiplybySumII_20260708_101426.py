# Last updated: 7/8/2026, 10:14:26 AM
1class Solution:
2    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
3        MOD = 10**9 + 7
4
5        pos = []
6        digits = []
7
8        for i, ch in enumerate(s):
9            if ch != '0':
10                pos.append(i)
11                digits.append(int(ch))
12
13        k = len(digits)
14
15        pow10 = [1] * (k + 1)
16        for i in range(1, k + 1):
17            pow10[i] = (pow10[i - 1] * 10) % MOD
18
19        prefVal = [0] * (k + 1)
20        prefSum = [0] * (k + 1)
21
22        for i in range(k):
23            prefVal[i + 1] = (prefVal[i] * 10 + digits[i]) % MOD
24            prefSum[i + 1] = prefSum[i] + digits[i]
25
26        ans = []
27
28        for l, r in queries:
29            L = bisect_left(pos, l)
30            R = bisect_right(pos, r) - 1
31
32            if L > R:
33                ans.append(0)
34                continue
35
36            cnt = R - L + 1
37
38            x = (
39                prefVal[R + 1]
40                - prefVal[L] * pow10[cnt]
41            ) % MOD
42
43            digit_sum = prefSum[R + 1] - prefSum[L]
44
45            ans.append((x * digit_sum) % MOD)
46
47        return ans