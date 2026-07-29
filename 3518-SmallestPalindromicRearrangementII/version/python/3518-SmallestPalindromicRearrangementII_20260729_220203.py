# Last updated: 7/29/2026, 10:02:03 PM
1from typing import List, Optional
2class Solution:
3    def count_perms(self, freq, cap: int) -> int:
4        n = sum(freq)
5        if n == 0:
6            return 1
7        ways = 1
8        remaining = n
9        for f in freq:
10            if f == 0:
11                continue
12            choose = f if f <= remaining - f else remaining - f
13            for i in range(choose):
14                ways = ways * (remaining - i) // (i + 1)
15                if ways >= cap:          
16                    return cap
17            remaining -= f
18        return ways
19    def kth_permutation(self, freq: List[int], k: int) -> Optional[str]:
20        if self.count_perms(freq, k) < k:  
21            return None
22        result = []
23        remaining = sum(freq)
24        while remaining > 0:
25            for c in range(26):
26                if freq[c] == 0:
27                    continue
28                freq[c] -= 1
29                ways = self.count_perms(freq, k)  
30                if k > ways:
31                    k -= ways          
32                    freq[c] += 1
33                else:
34                    result.append(chr(ord('a') + c))
35                    remaining -= 1
36                    break
37            else:
38                return None
39
40        return ''.join(result)
41
42    def smallestPalindrome(self, s: str, k: int) -> str:
43        n = len(s)
44        if n == 1:
45            return s if k == 1 else ""
46
47        freq = [0] * 26
48        for ch in s:
49            freq[ord(ch) - ord('a')] += 1
50
51        half = [0] * 26
52        mid = ""
53        for c in range(26):
54            if freq[c] % 2 == 1:
55                mid = chr(ord('a') + c)
56            half[c] = freq[c] // 2
57
58        if sum(half) == 0:
59            return mid if k == 1 else ""
60
61        left = self.kth_permutation(half, k)
62        if left is None:
63            return ""
64
65        return left + mid + left[::-1]