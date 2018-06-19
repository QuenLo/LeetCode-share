class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_Jump = 0
        for n in range(len(nums)):
            if nums[n] != 0:
                if n + nums[n] >= len(nums)-1:
                    return True
                tmp = self.checkzero(nums, n + nums[n])
                max_Jump = max(tmp, max_Jump)
            else:
                if max_Jump > n:
                    continue
                elif max_Jump == n:
                    if max_Jump == len(nums)-1:
                        return True
                    else:
                        return False  
                else:
                    return False
        return True
    def checkzero(self, nums, n):
        if nums[n] != 0:
            return n
        else:
            return self.checkzero(nums, n-1)
