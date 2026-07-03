# Last updated: 7/3/2026, 12:45:27 PM
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        d=str(digit)
        for i in range(len(nums)):
            s = str(nums[i])
            count+=s.count(d)
        return count
            
        