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
        DictE = { employee.id:employee for employee in employees }
        
        SelectL = [id]
        Total = 0
        while SelectL:
            select = SelectL.pop()
            Total += DictE[select].importance
            for sub in DictE[select].subordinates:
                SelectL.append(sub)
        return Total
