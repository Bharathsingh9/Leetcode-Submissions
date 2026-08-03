class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        pattern = list(pattern)
        if len(pattern)!=len(s):
            return False
        g = set(zip(s, pattern))
        return len(g) == len(set(s)) == len(set(pattern))