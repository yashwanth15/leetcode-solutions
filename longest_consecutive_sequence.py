class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result,temp=0,1
        uni=set(nums)
        for i,num in enumerate(nums):
            current=num+1
            if current in uni and current-2 not in uni:
                temp=1
                while current in uni:
                    current+=1
                    temp+=1
            result=max(temp,result)
        return result
        