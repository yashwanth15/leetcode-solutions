class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         listSet = set(nums)
         if len(listSet)==len(nums):
            return False
         return True