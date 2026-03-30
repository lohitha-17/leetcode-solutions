class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit    

        return max_profit
    

# Test cases
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
print(sol.maxProfit([1, 2, 3, 4, 5]))  # Expected: 4
print(sol.maxProfit([7, 6, 4, 3, 1]))  # Expected: 0    