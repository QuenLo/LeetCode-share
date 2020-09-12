class Solution:
    
    def find_set( self, start, left, need ):
        
        if left == 0:
            return []
        
        all_set = []
        for i in range( start, 10 ):
            if left == 1 and need == i:
                return  [ [i] ] 
            elif left > 1 and (need - i) > i:
                for subset in self.find_set( i+1, left-1, need-i ):
                    all_set.append( [i]+subset )
            elif need < i:
                return all_set

        return all_set
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        return self.find_set( 1, k, n )
