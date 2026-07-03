# Last updated: 7/3/2026, 12:45:28 PM
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum = 0
        squaresum = 0
        s = str(n)
        for i in range(len(s)):
            digitsum += int(s[i])
            squaresum += int(s[i])*int(s[i])
        if squaresum - digitsum >= 50:
            return True
        else:
            return False