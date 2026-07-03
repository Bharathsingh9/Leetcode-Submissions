# Last updated: 7/3/2026, 12:45:31 PM
from collections import defaultdict
class Solution:
    def getLength(self, nums: List[int]) -> int:
        d = nums
        n = len(nums)
        ans = 1
        for i in range(n):
            frequency = defaultdict(int)
            maxi = 0
            for j in range(i, n):
                x = nums[j]
                frequency[x] += 1
                maxi = max(maxi, frequency[x])
                length = j - i + 1
                if length == 1:
                    continue
                if len(frequency) == 1:
                    ans = max(ans, length)
                    continue
                if maxi % 2:
                    continue
                h = maxi // 2
                h1 = False
                valid = True
                for f in frequency.values():
                    if f == maxi:
                        pass
                    elif f == h:
                        h1 = True
                    else:
                        valid = False
                        break
                if valid and h1:
                    ans = max(ans, length)

        return ans
                