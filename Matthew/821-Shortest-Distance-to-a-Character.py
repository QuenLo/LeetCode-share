class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        site = len(S)
        output = []
        pre_pending = []
        pos_pending = []
        for ind in range(len(S)):
            if S[ind] == C:
                site = ind
                pos_pending += [0]
                pre_pending += [0]
                output += [min(pre_pending[z], pos_pending[z]) for z in range(len(pre_pending))]
                pre_pending = []
                pos_pending = []
            else:
                pre_pending += [abs(ind - site)]
                pos_pending = [z+1 for z in pos_pending] + [1]
        output += pre_pending
        return output
