# Last updated: 7/3/2026, 12:47:15 PM
class Solution:
  def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    ans = 0
    summ = 0

    for num in nums:
      if num == 0:
        summ = 0
      else:
        summ += num
        ans = max(ans, summ)

    return ans