class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # num1 = "1+-1i", num2 = "1+-1i"
        
        num1_1 = num1.split( "+" )
        real_1 = int(num1_1[0])
        imaginary_1 = int(num1_1[1][:-1])
        
        num2_1 = num2.split( "+" )
        real_2 = int(num2_1[0])
        imaginary_2 = int(num2_1[1][:-1])
        
        real_final = ( real_1*real_2 ) - (imaginary_1*imaginary_2)
        imaginary_final = ( real_1*imaginary_2 ) + ( real_2*imaginary_1 )
        
        return str(real_final) + "+" + str(imaginary_final) + "i"
