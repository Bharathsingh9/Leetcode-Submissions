class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 1
        min_prod = 1

        global_max = float('-inf')

        for num in nums :
            temp_max = max_prod
            temp_min = min_prod

            max_prod = max(
                num,
                temp_max * num,
                temp_min * num
            )

            min_prod = min(
                num,
                temp_max * num,
                temp_min * num
            )
            global_max = max(global_max , max_prod)
        return global_max