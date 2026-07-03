# Last updated: 7/3/2026, 12:45:57 PM
class Solution(object):
    def largestOddNumber(self, num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2==1:
                return num[:i+1]
        return ""

        