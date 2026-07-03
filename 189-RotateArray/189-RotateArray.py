# Last updated: 7/3/2026, 12:47:40 PM
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        nums.reverse()
        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])