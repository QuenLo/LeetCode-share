class Solution:
    def coinChange(self, coins, amount):
        value_list = [amount+1] * (amount+1)
        value_list[0] = 0
        
        for i in range( 1, amount+1 ):
            for coin in coins:
                if i >= coin:
                    value_list[i] = min( value_list[i-coin] + 1, value_list[i] )
        
        return -1 if value_list[amount] == amount + 1 else value_list[amount]
        
        
# solution II
class SolutionII:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float( 'inf' ) #infinite large
        coin_num = [0] + [MAX]*amount
        
        for i in range(1,amount+1):
            coin_num[i] = min( [ coin_num[i - c]  if  i - c >=0 else MAX for c in coins ] ) + 1
        

        return [coin_num[amount], -1][coin_num[amount]==MAX]
