class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j>i:
                    profit=prices[j]-prices[i]
                    if profit>maxp:
                        maxp=profit
        return maxp