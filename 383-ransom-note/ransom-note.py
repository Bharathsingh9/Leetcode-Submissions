class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm1 = {}
        hm2 = {}
        for i in ransomNote:
            hm1[i] = hm1.get(i,0)+1
        for j in magazine:
            hm2[j] = hm2.get(j,0)+1
        for k in hm1:
            if k not in hm2 or hm2[k] < hm1[k] :
                return False
        return True           