# Last updated: 7/3/2026, 12:48:11 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2 : ]