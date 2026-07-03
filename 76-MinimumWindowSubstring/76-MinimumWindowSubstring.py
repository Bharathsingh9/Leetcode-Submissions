# Last updated: 7/3/2026, 12:48:05 PM
class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        count = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            if s[right] in need:
                if need[s[right]] > 0:
                    count += 1
                need[s[right]] -= 1

            while count == len(t):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] > 0:
                        count -= 1
                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]
