class Solution:
    def canJump(self, nums):

        # if it never get into 0, then it will always reach the last index
        for i in range( 0,len(nums)-1 ):
            # the step = 0
            if nums[i] == 0:
                # if there is another way to skip this index
                for x in range( i-1, -2, -1 ):
                    # NO
                    if ( x < 0):
                        return False
                    # YES
                    elif ( nums[x] > ( i-x ) ):
                        break

        return True
        
