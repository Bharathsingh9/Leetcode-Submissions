# Last updated: 7/24/2026, 8:37:06 PM
1class Solution:
2    def uniqueXorTriplets(self, nums: List[int]) -> int:
3        return  1 if  len(sn:= set(nums))<2  else len({
4            x^y for x in {a^b for a,b in combinations(sn,2)} for y in sn
5        })
6        