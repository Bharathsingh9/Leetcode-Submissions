# Last updated: 7/3/2026, 12:48:51 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        f = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def cross(a, b):
            ans = []
            for i in a:
                for j in b:
                    ans.append(i + j)
            return ans

        li = f[digits[0]]
        i = 1

        while i < len(digits):
            li = cross(li, f[digits[i]])
            i += 1

        return li