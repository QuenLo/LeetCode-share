class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        memo = {}
        def paint( point, color ):
            
            if (point, color) in memo:
                return memo[ (point, color) ]
            
            total_cost = costs[point][color]
            if point == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min( paint(point+1, 1), paint(point+1, 2) )
            elif color == 1:
                total_cost += min( paint(point+1, 0), paint(point+1, 2) )
            elif color == 2:
                total_cost += min( paint(point+1, 1), paint(point+1, 0) )
                
            memo[ (point, color) ] = total_cost
            return total_cost
        
        if len(costs) == 0:
            return 0
        
        return min( paint(0,0), paint(0,1), paint(0,2) )



## Time Limit Exceeded
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        def paint( point, color ):
            
            total_cost = costs[point][color]
            if point == len(costs) - 1:
                pass
            elif color == 0:
                total_cost += min( paint(point+1, 1), paint(point+1, 2) )
            elif color == 1:
                total_cost += min( paint(point+1, 0), paint(point+1, 2) )
            elif color == 2:
                total_cost += min( paint(point+1, 1), paint(point+1, 0) )
                
            return total_cost
        
        if len(costs) == 0:
            return 0
        
        return min( paint(0,0), paint(0,1), paint(0,2) )
