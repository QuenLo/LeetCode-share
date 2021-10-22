# Time complexity : O(n + m)
# Space: O(m)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n < 1:
            return
        
        if (m) < 1:
            nums1[:] = nums2[:]
            return
        
        
        nums1_copy = nums1[:m]
        l, k = 0, 0
        
        for p in range( m+n ):
            
            if( (l < m and k < n and nums1_copy[l] <= nums2[k]) or k >= n ):
                nums1[p] = nums1_copy[l]
                l += 1
            else:
                nums1[p] = nums2[k]
                k += 1
        


class SolutionII:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n < 1:
            return
        
        if (m) < 1:
            nums1[:] = nums2[:]
            return
        
        
        nums1_copy = nums1[:]
        l, k = 0, 0
        
        while l < (m) or k < n:
            if ( k >= n ):
                nums1[l+k] = nums1_copy[l]
                l += 1
            elif ( l >= (m) ):
                nums1[l+k] = nums2[k]
                k+= 1
            elif ( nums1_copy[l] <= nums2[k] ):
                nums1[l+k] = nums1_copy[l]
                l += 1
            elif( nums1_copy[l] > nums2[k] ):
                nums1[l+k] = nums2[k]
                k += 1
        
