class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_Jump = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                if n + nums[n] > max_Jump:
                    max_Jump = n + nums[n]
            else:
                if max_Jump > n:
                    n = max_Jump
                elif max_Jump == n:
                    if max_Jump == len(nums)-1:
                        return True
                    else:
                        return False  
                else:
                    return False
        return True
