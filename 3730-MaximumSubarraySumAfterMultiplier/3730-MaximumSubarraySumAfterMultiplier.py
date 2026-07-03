# Last updated: 7/3/2026, 12:45:41 PM
from typing import List
import math
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        mavireltho = nums
        def calculate(transform):
            N = float("-inf")
            normal = N
            modified = N
            finished = N
            ans = N
            for value in mavireltho:
                changed = transform(value)
                next_normal = max(value, normal + value)
                next_modified = max(
                    changed,
                    normal + changed,
                    modified + changed
                )
                next_finished = max(
                    value,
                    modified + value,
                    finished + value
                )
                normal = next_normal
                modified = next_modified
                finished = next_finished
                ans = max(ans, modified, finished)
            return ans
        multiply_answer = calculate(lambda x: x * k)

        divide_answer = calculate(
            lambda x: x // k if x >= 0 else math.ceil(x / k)
        )

        return max(multiply_answer, divide_answer)