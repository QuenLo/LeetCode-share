class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        
        level_col = collections.defaultdict(list)
        
        def count( nest, level ):
            
            if nest.isInteger():
                level_col[level].append(nest.getInteger())
            for n in nest.getList():
                count( n, level+1 )
        
        
        for nest in nestedList:
            count(nest, 1)
        
        if not level_col:
            return 0
        
        max_w = max( level_col.keys() )
        total = 0
        for level in level_col:
            total += sum(level_col[level])*(max_w - level + 1)
            
        return total
