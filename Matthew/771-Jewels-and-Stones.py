class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return (len(re.split(''.join([str(n)+'|' for n in J]),S))-1)
