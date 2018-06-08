class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """  
#         for triangle in itertools.combinations(points, 3):
#             print (triangle[0], triangle[1], triangle[2], self.area(triangle[0], triangle[1], triangle[2]))
            
        return max([self.area(triangle[0], triangle[1], triangle[2]) for triangle in itertools.combinations(points, 3)])
    
    def area(self, a, b, c):
        b_vec = list(map(lambda x: x[0]-x[1], zip(b, a)))
        c_vec = list(map(lambda x: x[0]-x[1], zip(c, a)))
        area = abs(b_vec[0]*c_vec[1] - c_vec[0]*b_vec[1])/2
        return area
