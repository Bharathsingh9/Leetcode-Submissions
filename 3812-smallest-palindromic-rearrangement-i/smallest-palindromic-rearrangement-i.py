class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        n = len(s)
        mid = n//2
        if n%2 == 0:
            c = sorted(s[:mid])
            d = c[::-1]
            return "".join(c+d)
        elif n%2 == 1:
            f = sorted(s[:mid])
            g = f[::-1]
            return "".join(f+list(s[mid])+g)