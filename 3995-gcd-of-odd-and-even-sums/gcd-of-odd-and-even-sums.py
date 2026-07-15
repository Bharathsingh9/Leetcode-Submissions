class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumi=0
        sumii=0
        for i in range(1,n*2+1):
            if i%2==0:
                sumi+=i
            else:
                sumii+=i
        
        return n
        
