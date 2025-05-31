class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater=0
        i,j=0,len(heights)-1
        while i<j:
            water=(j-i)*min(heights[i],heights[j])
            maxWater=max(water,maxWater)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return maxWater
        