class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        profit=0
        while i<j and j<len(prices):
            if prices[j]<prices[i]:
                i=j
                j+=1
            else:
                diff = prices[j]-prices[i]
                profit=max(diff,profit)
                j+=1
        return profit