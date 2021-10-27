## Hash map
# n be the length of the input array and L be the number of non-zero elements.
# Time: O(n) for creating the Hash Map; O(L) for calculating the dot product.
# Space: O(1)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i, value in enumerate(nums):
            if value:
                self.nonzeros[i] = value

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        result = 0
        for num in self.nonzeros:
            if num in vec.nonzeros:
                result += self.nonzeros[num]*vec.nonzeros[num]
        
        return result

## Non-efficient Array Approach
# Time: O(n) for both constructing the sparse vector and calculating the dot product.
# Space: O(1)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.array = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        result = 0
        for num1, num2 in zip(self.array, vec.array):
            result += num1*num2
        
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
