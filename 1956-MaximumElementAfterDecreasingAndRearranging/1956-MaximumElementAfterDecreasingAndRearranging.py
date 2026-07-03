# Last updated: 7/3/2026, 12:46:00 PM
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        max_val = 1
        for i in range(1, len(arr)):
            if arr[i] > max_val:
                max_val += 1
        return max_val