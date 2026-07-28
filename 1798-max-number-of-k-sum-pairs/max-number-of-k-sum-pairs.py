class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hm ={}
        count = 0
        for i in nums:
            s = k - i
            if s in hm and hm.get(s,0)>0:
                hm[s]-=1
                count+=1
            else:
                hm[i] = hm.get(i,0)+1
        return count
        
