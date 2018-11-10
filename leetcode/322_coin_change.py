class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        ways = [float('inf')] * (amount+1)
        ways[0] = 0
        
        for c, coin in enumerate(coins):
            for x in range(coin, amount+1):
                ways[x] = min(ways[x], 1+ways[x-coin])
        return ways[-1] if ways[-1] != float('inf') else -1

import pdb
pdb.set_trace()
coins, amount = [1,2,5], 11
print(Solution().coinChange(coins,amount))
coins, amount = [2], 3
print(Solution().coinChange(coins,amount))
