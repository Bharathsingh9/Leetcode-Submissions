# Last updated: 7/3/2026, 12:45:33 PM
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def checkPrime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for d in range(3, int(x**0.5) + 1, 2):
                if x % d == 0:
                    return False
            return True
        
        operations = 0
        index = 0
        
        while index < len(nums):
            if index % 2 == 0:
                if not checkPrime(nums[index]):
                    nums[index] += 1
                    operations += 1
                    continue
                else:
                    index += 1
            else:
                if checkPrime(nums[index]):
                    operations += 1
                    nums[index] += 1
                    continue
                else:
                    index += 1

        return operations
        