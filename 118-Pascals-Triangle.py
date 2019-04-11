class Solution(object):
    def generate(self, numRows):

        if numRows == 0:
            return []
        
        Ans = []
        Ans.append([1])
        for i in range(1,numRows):
            Ans.append([])
            a = 1
            Ans[i].append(1)
            while a < i:
                Ans[i].append( Ans[i-1][a-1]+Ans[i-1][a] )
                a += 1
            Ans[i].append(1)
                
        return Ans
        
# solution II
class SolutionII(object):
    def generate(self, numRows):

        Ans = []
        for i in range(numRows):
            if i <= 1:
                pre =  [1]*(i+1)
                Ans.append( pre )
            else:
                temp = [1]
                for y in range( 1,i ):
                    temp.append( pre[y-1]+pre[y] )
                pre = temp + [1]
                Ans.append(pre)
        return Ans
