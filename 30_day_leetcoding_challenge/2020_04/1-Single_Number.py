class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        #solution 1
        # return sum( set( nums ) )*2 - sum( nums )
        
        #solution 2
        # rest = {}
        # for num in nums:
        #     try:
        #         rest[num] += 1
        #     except KeyError:
        #         rest[num] = 1
        # for num in rest:
        #     if rest[num] == 1:
        #         return num
        
        #solution 3
        rest = 0
        for num in nums:
            rest ^= num
        return rest
