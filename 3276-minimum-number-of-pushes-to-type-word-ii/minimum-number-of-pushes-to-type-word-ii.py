class Solution:
    def minimumPushes(self, word: str) -> int:
        f = [0] * 26
        for k in word:
            f[ord(k) - ord('a')] += 1
        f.sort(reverse=True)
        r = 0
        for i in range(26):
            if f[i] == 0:
                break
            r += f[i] * (i // 8 + 1)
        return r