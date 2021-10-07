class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        while sx <= tx and sy <= ty:
            if ty == tx:
                break
            
            if ty > tx:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
            else:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
        
        return tx == sx and ty == sy

## Work Backwards (Naive Variant) [Time Limit Exceeded]
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        while sx <= tx and sy <= ty:
            if sx == tx and sy == ty: return True
            if tx > ty:
                tx = tx - ty
            else:
                ty = ty -tx
        
        return False
