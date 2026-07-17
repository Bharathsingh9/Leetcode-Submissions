class Solution:
    def reverseWords(self, s: str) -> str:
        g = s.split()
        c = g[::-1]
        return " ".join(c)