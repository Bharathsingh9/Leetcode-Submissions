# Last updated: 7/3/2026, 12:45:30 PM
class Solution:
    def maxValue(self, nums1: list[int], nums0: list[int]) -> int:
        arr = []

        for i in range(len(nums1)):
            arr.append('1' * nums1[i] + '0' * nums0[i])

        def customCompare(x, y):
            if x + y > y + x:
                return -1
            elif x + y == y + x:
                return 0
            else:
                return 1

        arr.sort(key=cmp_to_key(customCompare))

        final_str = "".join(arr)

        MOD = 10**9 + 7
        ans = 0
        for ch in final_str:
            ans = (ans * 2 + int(ch)) % MOD

        return ans