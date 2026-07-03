# Last updated: 7/3/2026, 12:49:06 PM
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            sign=-1
        else:
            sign=1
        x=x*sign
        reverse = 0
        while x!=0:
            reverse = reverse*10+x%10
            x=x//10
        reverse=reverse*sign
        if reverse<-2**31 or reverse>2**31-1:
            return 0
        return reverse 