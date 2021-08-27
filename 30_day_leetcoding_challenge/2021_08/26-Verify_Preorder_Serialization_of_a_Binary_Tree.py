class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        
        #Preorder (Root, Left, Right)
        cnt = 0
        preorder_l = preorder.split(',')
        for s in preorder_l[:-1]:
            if s == '#':
                cnt -= 1
                if cnt < 0: return False
            else:
                cnt += 1
                
        return cnt == 0 and preorder_l[-1] == '#'
