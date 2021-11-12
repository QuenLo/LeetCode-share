class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        def helper( mat, first ):
            mat_dict = collections.defaultdict(dict)
            for r, row in enumerate(mat):
                for c, value in enumerate(row):
                    if value != 0:
                        if first:
                            mat_dict[r][c] = value
                        else:
                            mat_dict[c][r] = value
                            
            return mat_dict
        
        mat1_d = helper(mat1, True)
        mat2_d = helper(mat2, False)
        m, n = len(mat1), len(mat2[0])
        ans = [ [ 0 for _ in range(n) ] for _ in range(m) ]
        
        for r in mat1_d:
            for c in mat2_d:
                ans[r][c] = sum( mat1_d[r][k]*mat2_d[c][k] for k in mat1_d[r] if k in mat2_d[c] )
                
        return ans


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])
        
        def count( m_i, k_i ):
            
            su_sum = 0
            for m1 in range(k):
                su_sum += mat1[m_i][m1] * mat2[m1][k_i]
            
            # print(m_i, k_i, su_sum)
            return su_sum
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for m_i in range(m):
            for k_i in range(n):
                ans[m_i][k_i] = count( m_i, k_i )
        
        return ans
