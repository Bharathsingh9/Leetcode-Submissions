# Last updated: 7/9/2026, 2:00:04 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        row = [1] * (rowIndex + 1)
4        for i in range(2, rowIndex + 1):
5            for j in range(i - 1, 0, -1):
6                row[j] += row[j - 1]
7        return row