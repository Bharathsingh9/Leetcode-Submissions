# Last updated: 7/3/2026, 12:47:48 PM
class Solution(object):
    def reverseWords(self, s):
        c=s.split()[::-1]
        return " ".join(c)
