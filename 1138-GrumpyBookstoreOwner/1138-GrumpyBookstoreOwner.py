# Last updated: 7/3/2026, 12:46:43 PM
class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        sumi=0
        for i,j in zip(customers,grumpy):
            if j==0:
                sumi+=i
        extra=0
        max_extra=0
        l = 0
        cur = 0
        for r in range(len(grumpy)):
            if grumpy[r] == 1:
                cur += customers[r]
            if (r-l+1) > minutes:
                if grumpy[l] == 1:
                    cur -= customers[l]
                l += 1
            max_extra = max(max_extra,cur)
        return sumi + max_extra                





        