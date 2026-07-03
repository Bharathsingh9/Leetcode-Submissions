# Last updated: 7/3/2026, 12:46:18 PM
class Solution(object):
    def maxVowels(self, s, k):
        v="aeiou"
        count=0
        for ch in s[:k].lower():
            if ch in v:
                count+=1
        max_count=count
        for i in range(k,len(s)):
            if s[i].lower() in v:
                count+=1
            if s[i-k].lower() in v:
                count-=1
            max_count=max(max_count,count)
        return max_count



        