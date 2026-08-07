class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        r = 0
        for i in s + t:
            r ^= ord(i)
        return chr(r)