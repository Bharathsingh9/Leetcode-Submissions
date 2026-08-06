class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i = n
        while True:
            r = 1
            for j in str(i):
                r = r * int(j)
            if r % t == 0:
                return i
            i += 1