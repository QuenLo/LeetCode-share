"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):

        for employee in employees:
            if employee.id == id:
                if employee.subordinates != []:
                    for subordinate in employee.subordinates:
                        employee.importance += self.getImportance(employees,subordinate)
                    return employee.importance
                return employee.importance
        
        return 0
