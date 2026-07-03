# Last updated: 7/3/2026, 12:46:19 PM
class Solution(object):
    def maxScore(self, cardPoints, k):
        window_sum=sum(cardPoints[:k])
        maxi=window_sum
        total=sum(cardPoints)
        if k==len(cardPoints):
            return total
        right=len(cardPoints)-1
        for i in range(k-1,-1,-1):
            window_sum-=cardPoints[i]
            window_sum+=cardPoints[right]
            right-=1
            maxi=max(maxi,window_sum)
        return maxi

        