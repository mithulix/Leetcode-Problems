class Solution:
    def countHomogenous(self, s: str) -> int:
        res = 1
        c = 1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                c+=1
            else:
                c = 1
            res += c
        return (res)%(10**9+7)