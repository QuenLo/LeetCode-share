class Solution_ComplexNumber(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        walk = {'U':1,'D':-1,'L':1j,'R':-1j}
        
        return sum( walk[move] for move in moves ) == 0


class Solution(object):
    def judgeCircle(self, moves):

        walk = {'U':1,'L':1,'D':-1,'R':-1}
        stepLR, stepUD = 0, 0
        for move in moves:
            if move in ['L','R']:
                stepLR += walk[move]
            else:
                stepUD += walk[move]
        
        return (stepUD==0) & (stepLR==0)


class Solution_count(object):
    def judgeCircle(self, moves):
        
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


class Solution_collection(object):
    def judgeCircle(self, moves):

        walk = collections.Counter(moves)
        return walk['L'] == walk['R'] and walk['U'] == walk['D']
