# Last updated: 7/16/2026, 7:41:59 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        maxi = max(candies)   
4        l = []  
5        sumi = 0
6        for i in range(len(candies)):
7            sumi=candies[i]+extraCandies
8            if sumi >= maxi:
9                l.append(True)
10            else:
11                l.append(False)
12            sumi=0
13        return l