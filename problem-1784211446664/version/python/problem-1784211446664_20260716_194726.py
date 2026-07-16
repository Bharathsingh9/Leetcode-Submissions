# Last updated: 7/16/2026, 7:47:26 PM
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        maxi = max(candies)
4
5        for i in range(len(candies)):
6            candies[i] = candies[i] + extraCandies >= maxi
7
8        return candies