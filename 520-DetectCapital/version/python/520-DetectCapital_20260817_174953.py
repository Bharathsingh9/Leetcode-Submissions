# Last updated: 8/17/2026, 5:49:53 PM
1class Solution:
2    def detectCapitalUse(self, word: str) -> bool:
3        if word.isupper():
4            return True
5        if word.islower():
6            return True
7        if word[0].isupper() and word[1:].islower():
8            return True
9        return False