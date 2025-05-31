class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charCount={}
        for i in s:
            if i not in charCount:
                charCount[i]=1
            else:
                charCount[i]+=1
        for i in t:
            if i not in charCount:
                return False
            charCount[i]-=1
        for value in charCount.values():
            if value!=0:
                return False
        return True

        