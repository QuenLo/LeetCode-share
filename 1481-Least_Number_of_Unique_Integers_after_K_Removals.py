import collections

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        count = collections.Counter( arr )
        count_sort = dict( sorted( count.items(), key = lambda item: item[1]) )
        print(count_sort)
        
        ans = len(count)
        for c in count_sort:
            if count_sort[c] <= k:
                k -= count_sort[c]
                ans -= 1

        return ans
