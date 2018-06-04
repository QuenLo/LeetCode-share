class Solution(object):
    def checkPossibility(self, nums):
        
        ModifyingTimes = 0
        for i in range(1 , len(nums)) :

            if nums[i-1] > nums[i] :
                ModifyingTimes += 1

                # delete left one
                if nums[i-2] < nums[i] or i < 2 :
                    nums[i-1] = nums[i]
                # delete right one
                else:
                    nums[i] = nums[i-1]
                
            if ModifyingTimes > 1 :
                return False
        
        return True
