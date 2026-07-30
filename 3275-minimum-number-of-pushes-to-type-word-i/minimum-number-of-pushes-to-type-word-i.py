class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        r=0 
        p=1
        while n>=8:
            r+=(8*p)
            p+=1
            n-=8
        r+=(n*p)
        return r
            
            