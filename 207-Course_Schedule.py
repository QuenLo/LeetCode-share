class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        course_col = collections.defaultdict(list)
        for realate in prerequisites:
            nex, pre = realate[0], realate[1]
            course_col[ pre ].append(nex)
            
        checked = [False]*numCourses
        path = [False]*numCourses
        
        def isCyclic( currCourse ):
            
            if checked[ currCourse ]:
                return False
            if path[ currCourse ]:
                return True
            
            path[ currCourse ] = True
            k = False
            for child in course_col[ currCourse ]:
                k = isCyclic( child )
                if k: break
            path[ currCourse ] = False
            
            checked[ currCourse ] = True
            return k
        
        for numC in range(numCourses):
            if isCyclic(numC):
                return False
            
        return True
