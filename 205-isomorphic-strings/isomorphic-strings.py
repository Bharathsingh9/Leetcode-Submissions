class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        g = set(zip(s,t))
        print(g)
        return len(g) == len(set(s)) == len(set(t))
        