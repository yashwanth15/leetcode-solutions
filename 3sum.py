class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i,target in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            s=i+1
            l=len(nums)-1
            while s<l:
                val = target+nums[s]+nums[l]
                if val==0:
                    result.append([target,nums[s],nums[l]])
                    s+=1
                    l-=1
                    #to avoid duplicate triplets
                    while s<l and nums[s]==nums[s-1]:
                        s+=1
                    while s<l and nums[l]==nums[l+1]:
                        l-=1
                elif val<0:
                    s+=1
                else:
                    l-=1
        return result
        