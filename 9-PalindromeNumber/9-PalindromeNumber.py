# Last updated: 7/3/2026, 12:49:03 PM
class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        r=0
        s=x
        while x>0:
            r=r*10+(x%10)
            x=x//10
        if r==s:
            return True
        else:
            return False