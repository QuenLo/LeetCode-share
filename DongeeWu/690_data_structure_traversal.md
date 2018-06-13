# Problem
https://leetcode.com/problems/employee-importance/description/

# Python
```
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        mapping = {employee.id:employee for employee in employees}
        
        def iter(idNow):
            employeeNow = mapping[idNow]
            if len(employeeNow.subordinates) != 0:
                return sum([iter(sub) for sub in employeeNow.subordinates]) + employeeNow.importance
            else:
                return employeeNow.importance
              
        return iter(id)
      
      
      
        
        
```