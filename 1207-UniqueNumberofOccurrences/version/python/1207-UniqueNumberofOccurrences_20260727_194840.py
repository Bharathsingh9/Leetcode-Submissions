# Last updated: 7/27/2026, 7:48:40 PM
1class Solution:
2    def uniqueOccurrences(self, arr: List[int]) -> bool:
3        hm = {}
4        for i in range(len(arr)):
5            hm[arr[i]] = hm.get(arr[i], 0)+1
6        return len(hm.values()) == len(set(hm.values()))
7