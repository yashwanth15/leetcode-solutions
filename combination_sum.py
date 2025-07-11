class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]

        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target or i>=len(nums):
                return
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res
        