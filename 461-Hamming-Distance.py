class Solution:
    def hammingDistance(self, x, y):
    
        result = x^y
        return bin(result).count('1')
