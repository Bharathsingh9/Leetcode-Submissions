class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        n = len(nums)
        for i in range(n):
            left.append( left[-1]*nums[i] )
            right.insert(0, right[0]*nums[n-i-1] )
        output = []
        print("Left : ",left)
        print("Right : ",right)
        for i in range(n):
            output.append(
                left[i] * right[i+1]
            )
        return output