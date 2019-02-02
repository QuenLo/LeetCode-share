class Solution:
    def addBinary(self, a, b):

        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        
        if ( a[-1] == "1" and b[-1] == "1" ):
            return self.addBinary( self.addBinary( a[:-1], b[:-1] ), "1" ) + "0"
        elif( a[-1] == "0" and b[-1] == "0" ):
            return self.addBinary( a[:-1], b[:-1] ) + "0"
        else:
            return self.addBinary( a[:-1], b[:-1] ) + "1"
            
    ## second way
    # return bin(eval('0b'+a) + eval('0b'+b))[2:]
    
    ## third way
    # return ( bin(int(a,2)+int(b,2) ) )[2:]
