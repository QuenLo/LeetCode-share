#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        Ls, Ws = binaryMatrix.dimensions()
        Ls -= 1
        Ws -= 1
        ana = -1

        while( (Ls >= 0) and (Ws >= 0) ):
            if binaryMatrix.get( Ls, Ws ):
                ana = Ws
                Ws -= 1
            else:
                Ls -= 1

        return ana
