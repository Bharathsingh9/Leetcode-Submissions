# Last updated: 7/9/2026, 11:43:22 PM
1class Solution:
2    def convertToTitle(self, columnNumber: int) -> str:
3        output = ""
4        while columnNumber > 0:
5            output = chr(ord('A') + (columnNumber - 1) % 26) + output
6            columnNumber = (columnNumber - 1) // 26
7        return output