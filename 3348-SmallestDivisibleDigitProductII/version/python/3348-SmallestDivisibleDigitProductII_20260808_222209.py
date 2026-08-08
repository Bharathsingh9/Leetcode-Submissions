# Last updated: 8/8/2026, 10:22:09 PM
1class Solution:
2    def smallestNumber(self, num: str, t: int) -> str:
3        req2 = req3 = req5 = req7 = 0
4        temp = t
5        while temp % 2 == 0:
6            temp //= 2
7            req2 += 1
8        while temp % 3 == 0:
9            temp //= 3
10            req3 += 1
11        while temp % 5 == 0:
12            temp //= 5
13            req5 += 1
14        while temp % 7 == 0:
15            temp //= 7
16            req7 += 1
17        if temp > 1: return "-1"
18
19        dp = [[float('inf')] * 40 for _ in range(60)]
20        dp[0][0] = 0
21        
22        trans = [(1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2)]
23        for i in range(60):
24            for j in range(40):
25                if dp[i][j] == float('inf'):
26                    continue
27                for d2, d3 in trans:
28                    ni = min(59, i + d2)
29                    nj = min(39, j + d3)
30                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)
31                    
32        for i in range(59, -1, -1):
33            for j in range(39, -1, -1):
34                if i < 59:
35                    dp[i][j] = min(dp[i][j], dp[i + 1][j])
36                if j < 39:
37                    dp[i][j] = min(dp[i][j], dp[i][j + 1])
38
39        F2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
40        F3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
41        F5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
42        F7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
43
44        n = len(num)
45        has_zero = False
46        first_zero = n
47        for idx, char in enumerate(num):
48            if char == '0':
49                has_zero = True
50                first_zero = idx
51                break
52
53        if not has_zero:
54            r2, r3, r5, r7 = req2, req3, req5, req7
55            for char in num:
56                d = int(char)
57                r2 = max(0, r2 - F2[d])
58                r3 = max(0, r3 - F3[d])
59                r5 = max(0, r5 - F5[d])
60                r7 = max(0, r7 - F7[d])
61            if r2 == 0 and r3 == 0 and r5 == 0 and r7 == 0:
62                return num
63
64        limit = min(n - 1, first_zero)
65        p2 = p3 = p5 = p7 = 0
66        for i in range(limit):
67            d = int(num[i])
68            p2 += F2[d]
69            p3 += F3[d]
70            p5 += F5[d]
71            p7 += F7[d]
72
73        for i in range(limit, -1, -1):
74            start_d = int(num[i]) + 1
75            for d in range(start_d, 10):
76                n2 = max(0, req2 - p2 - F2[d])
77                n3 = max(0, req3 - p3 - F3[d])
78                n5 = max(0, req5 - p5 - F5[d])
79                n7 = max(0, req7 - p7 - F7[d])
80                L = n - 1 - i
81                
82                if n7 + n5 + dp[n2][n3] <= L:
83                    ans_list = list(num[:i]) + [str(d)]
84                    rem2, rem3, rem5, rem7 = n2, n3, n5, n7
85                    for pos in range(L):
86                        for x in range(1, 10):
87                            nn2 = max(0, rem2 - F2[x])
88                            nn3 = max(0, rem3 - F3[x])
89                            nn5 = max(0, rem5 - F5[x])
90                            nn7 = max(0, rem7 - F7[x])
91                            if nn7 + nn5 + dp[nn2][nn3] <= L - 1 - pos:
92                                ans_list.append(str(x))
93                                rem2, rem3, rem5, rem7 = nn2, nn3, nn5, nn7
94                                break
95                    return "".join(ans_list)
96            
97            if i > 0:
98                d = int(num[i - 1])
99                p2 -= F2[d]
100                p3 -= F3[d]
101                p5 -= F5[d]
102                p7 -= F7[d]
103
104        min_len_needed = req7 + req5 + dp[req2][req3]
105        M = max(n + 1, min_len_needed)
106        ans_list = []
107        rem2, rem3, rem5, rem7 = req2, req3, req5, req7
108        
109        for pos in range(M):
110            for x in range(1, 10):
111                nn2 = max(0, rem2 - F2[x])
112                nn3 = max(0, rem3 - F3[x])
113                nn5 = max(0, rem5 - F5[x])
114                nn7 = max(0, rem7 - F7[x])
115                if nn7 + nn5 + dp[nn2][nn3] <= M - 1 - pos:
116                    ans_list.append(str(x))
117                    rem2, rem3, rem5, rem7 = nn2, nn3, nn5, nn7
118                    break
119        return "".join(ans_list)