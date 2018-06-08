class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mistake = 0
        x = nums[0]
        nums.append(max(nums))
        nums.insert(0, 0)
        for n in range(2,len(nums)):
            if mistake <2:
                if x <= nums[n]:
                    x = nums[n]
                else:
                    mistake += 1
                    if x <= nums[n+1] or nums[n] >= nums[n-2]:
                        x = nums[n]
                    else:
                        return False
            else:
                return False
        return True
        
