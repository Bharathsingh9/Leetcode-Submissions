class Solution:
    def isHappy(self, n: int) -> bool:
        if n<10:
            if n == 1 or n == 7:
                return True
            else:
                return False
        def ans(m):
            if m<10:
                if m == 1 or m == 7:
                    return True
                else:
                    return False
            i = 0
            while m > 0:
                j = m % 10
                i += j * j
                m = m // 10
            if i == 1:
                return True
            else:
                return ans(i)
        return ans(n)
        
    