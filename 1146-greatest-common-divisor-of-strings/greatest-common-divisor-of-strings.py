class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        n=len(str1)
        m=len(str2)
        if n>m:
            str1,str2=str2,str1
        n=len(str1)
        m=len(str2)
        
        
        for i in range(n-1,-1,-1):
            v = str1[:i+1]
            g = len(v)
            if n % g != 0 or m % g != 0:
                continue
            if v*(n//g) == str1 and v*(m//g) == str2:
                return v
        return ""
            