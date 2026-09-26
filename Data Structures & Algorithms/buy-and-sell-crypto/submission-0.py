class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        profit=0
        while j<len(prices):
            if prices[i] < prices[j]:
                profit=max(profit,(prices[j]-prices[i]))
                j+=1
            elif prices[i] >= prices[j]:
                i+=1
                j=i+1
        return profit

        