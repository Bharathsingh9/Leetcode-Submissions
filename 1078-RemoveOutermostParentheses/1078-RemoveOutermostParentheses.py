# Last updated: 7/3/2026, 12:46:44 PM
class Solution(object):
    def removeOuterParentheses(self, s):
        result=""
        l=0
        for i in s:
            if i=="(":
                if l>0:
                    result+=i
                l+=1
            elif i==")":
                l-=1
                if l>0:
                    result+=i
        return result


        