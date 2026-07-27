class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        for i in range(len(arr)):
            hm[arr[i]] = hm.get(arr[i], 0)+1
        return len(hm.values()) == len(set(hm.values()))
