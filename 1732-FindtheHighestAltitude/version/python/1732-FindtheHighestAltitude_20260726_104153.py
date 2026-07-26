# Last updated: 7/26/2026, 10:41:53 AM
1class Solution:
2    def largestAltitude(self, gain: List[int]) -> int:
3        for i in range(len(gain)-1):
4            gain[i+1] = gain[i]+gain[i+1]
5        if max(gain)<0:
6            return 0
7        else:
8            return max(gain)