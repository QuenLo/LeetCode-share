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
    
# solution with BFS
class SolutionIII:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = [False]*(amount+1)
        visited[0] = True
        coin_num = 0
        value_now, value_next = [0], []
        
        while value_now:
            coin_num += 1
            for value in value_now:
                for coin in coins:
                    newvalue = value + coin
                    if newvalue == amount:
                        return coin_num
                    elif newvalue > amount:
                        continue
                    elif not visited[newvalue]:
                        visited[newvalue] = True
                        value_next.append( newvalue )
            value_now, value_next = value_next, []
            
        return -1
    
# solution with DFS
class SolutionIIV:
    def coinChange(self, coins, amount):
        coins.sort( reverse = True)
        lenc, self.min_step = len(coins), float('inf')
        
        def dfs( point, amo , count ):
            if not amo: #amount != 0
                self.min_step = min( self.min_step, count )
            for i in range( point, lenc ):
                if coins[i] <= amo < coins[i] * (self.min_step - count):
                    dfs( i, amo-coins[i], count+1 )
            
        for i in range( lenc ):
            dfs( i, amount, 0 )
    
        return [self.min_step, -1][ self.min_step == float('inf') ]
    
# solution with DFS, interative
class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        lenc, min_steps = len(coins), float('inf')
        dfs_stack = [ (0, 0, lenc) ]
        
        while len(dfs_stack) != 0:
            steps, value_now, coins_num = dfs_stack.pop()
            if value_now == amount:
                min_steps = min( min_steps, steps )
            if value_now > amount or amount - value_now > coins[ coins_num-1 ] * (min_steps - steps):
                continue
            for coinnum, coin in enumerate( coins[:coins_num] ):
                dfs_stack.append( (steps+1, value_now + coin, coinnum + 1) )
                
        return min_steps if min_steps != float('inf') else -1
