# Last updated: 8/15/2026, 8:26:26 PM
1class Solution:
2    def elevatorRequests(self, n: int, requests: list[int]) -> int:
3        d = requests[0]
4        for i in range(len(requests)-1):
5            d+=abs(requests[i]-requests[i+1])
6        return d