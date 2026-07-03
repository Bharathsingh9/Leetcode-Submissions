# Last updated: 7/3/2026, 12:48:56 PM
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=[]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                break
            ans.append(first[i])
        return "".join(ans)