class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)

        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies >= maxi

        return candies