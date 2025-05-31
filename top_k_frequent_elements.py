class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=[[] for i in range(len(nums)+1)]
        countMap=defaultdict(int)
        result=[]
        for i in nums:
            countMap[i]+=1
        for key,value in countMap.items():
            count[value].append(key)
        for i in range(len(count)-1,0,-1):
            for j in count[i]:
                result.append(j)
                if len(result)==k:
                    return result
