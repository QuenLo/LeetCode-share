class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        gap = [1]
        n = 0
        add = 2
        for z in seats:
            if z == 0:
                n += add
            else:
                add = 1
                gap.append(n)
                n = 0
        gap.append(n*2)
        return (math.ceil(max(gap)/2))
