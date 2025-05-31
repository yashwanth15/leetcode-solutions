class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,res=0,0
        seq=set()
        for r in range(len(s)):
            while s[r] in seq:
                seq.remove(s[l])
                l+=1
            seq.add(s[r])
            res=max(res,r-l+1)
        return res
