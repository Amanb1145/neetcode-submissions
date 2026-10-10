class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxp=0
        # for i in range(len(prices)):
        #     for j in range(len(prices)):
        #         if j>i:
        #             profit=prices[j]-prices[i]
        #             if profit>maxp:
        #                 maxp=profit
        # return maxp
        minpr=prices[0]
        maxp=0
        i=1
        while(i<len(prices)):
            pro=prices[i]-minpr
            if pro>maxp:
                maxp=pro
            if prices[i]<minpr:
                minpr=prices[i]
            i+=1
        return maxp