# Last updated: 7/3/2026, 12:47:32 PM
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n & n-1 == 0:
            return True
        else:
            return False
        