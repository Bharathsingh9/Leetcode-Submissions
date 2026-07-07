class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0 :
            return 0        
        x = ""
        sum_ = 0
        for i  in  str(n) :
            if i != '0' :
                sum_ += int(i)
                x = x + i
        return int(x) * sum_