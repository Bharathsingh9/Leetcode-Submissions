# Last updated: 8/15/2026, 9:09:14 PM
1class Solution:
2    def kthDigit(self, k: int) -> int:
3        if k <=9:
4            return k
5        k-=9
6        d=1
7        while True:
8            f = 10**(d-1)
9            l = 10**d-1
10            b = 10*(d+1)
11            n = l - f + 1
12            t = n*b
13            if k>t:
14                k-=t
15                d+=1
16            else:
17                break
18        bi = (k-1)//b
19        c = f+bi
20        p = (k-1)%b
21        ni = p//(d+1)
22        di = p%(d+1)
23        if c%2==0:
24            num = 10*c+ni
25        else:
26            num = 10*c+9-ni
27        return int(str(num)[di])