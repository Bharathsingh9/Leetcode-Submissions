# Last updated: 7/3/2026, 12:45:25 PM
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        res = 0
        nums.sort(reverse = True)
        for i in range(k):
            if mul > 0:
                res += nums[i]*mul
                mul -= 1
            else:
                res += nums[i]
        return res
                    