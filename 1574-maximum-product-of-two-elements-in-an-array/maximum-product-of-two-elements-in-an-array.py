class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')
        for i in nums:
            if i >= first_max:
                second_max = first_max
                first_max = i
            elif i > second_max:
                second_max = i
        return (first_max-1)*(second_max-1)
