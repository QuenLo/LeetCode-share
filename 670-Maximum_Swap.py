class Solution:
    def maximumSwap(self, num: int) -> int:
        
        nums_l = [ int(n) for n in str(num) ]
        for i in range( len(nums_l)-1 ):
            maxi = max( nums_l[i+1:] )
            if nums_l[i] < maxi:
                j = len(nums_l)-1
                while j > i and nums_l[j] != maxi:
                    j -= 1
                nums_l[i], nums_l[j] = nums_l[j], nums_l[i]
                break
        
        return int("".join( [ str(i) for i in nums_l ] ))
