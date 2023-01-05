class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i] - buy)
        return profit

# prices = [7,1,5,3,6,4] # Output: 5
# prices = [7,6,4,3,1] #Output: 0
# Solution().maxProfit(prices)
