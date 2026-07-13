class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = ""
        i=0
        j=0
        while i <= len(word1)-1 and j<=len(word2)-1:
            l+=word1[i]
            l+=word2[j]
            i+=1
            j+=1
        while i <= len(word1)-1:
            l+=word1[i]
            i+=1
        while j<=len(word2)-1:
            l+=word2[j]
            j+=1
        return l




