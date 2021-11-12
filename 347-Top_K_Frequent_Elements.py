# Time: O(Nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        count = collections.Counter(nums)
        return heapq.nlargest( k, count.keys(), key=count.get )

## QUICK SELECT      
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        count = collections.Counter(nums)
        unique = list( count.keys() )
        
        def partition(left, right, pivot_index):
            fre = count[unique[pivot_index]]
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]
            
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < fre:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
                    
            unique[right], unique[store_index] = unique[store_index], unique[right]
            return store_index
        
        def quick_select(left, right, k):
            
            if left == right:
                return
            
            pivot_index = random.randint(left,right)
            
            pivot_index = partition(left, right, pivot_index)
            
            if k < pivot_index:
                quick_select( left, pivot_index - 1, k )
                
            elif k > pivot_index:
                quick_select( pivot_index + 1, right, k )
            
            else:
                return
            
        n = len(unique)
        quick_select( 0, n-1, n-k )
        return unique[n-k:]
