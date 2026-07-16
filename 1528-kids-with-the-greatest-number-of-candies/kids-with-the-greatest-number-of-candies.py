class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)   
        l = []  
        sumi = 0
        for i in range(len(candies)):
            sumi=candies[i]+extraCandies
            if sumi >= maxi:
                l.append(True)
            else:
                l.append(False)
            sumi=0
        return l