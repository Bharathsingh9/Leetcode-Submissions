class Solution:
    def findGCD(self, nums: List[int]) -> int:
        i=1
        j=1
        a=[]
        b=[]
        M = float("-inf")
        N = float("inf")
        for k in range(len(nums)):
            M = max(M,nums[k])
            N = min(N,nums[k])
        while i<=M:
            if M%i == 0:
                a.append(i)
            i+=1
        while j<=N:
            if N%j == 0:
                b.append(j)  
            j+=1
        G = max(list(set(a) & set(b)))
        return G
        
        