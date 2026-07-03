# Last updated: 7/3/2026, 12:47:14 PM
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans=0
        sl=SortedList()
        for num in nums:
            idx=sl.bisect_right(num*2)
            ans+=len(sl)-idx
            sl.add(num)
        return ans