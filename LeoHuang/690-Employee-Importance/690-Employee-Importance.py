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
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    totalImportanceValue = 0
    # sub_ids stores subordinates' ids
    sub_ids = [id]
    idToEmployeesIndex = {}
    for i in range(len(employees)):
      idToEmployeesIndex[employees[i].id] = i
    while len(sub_ids) != 0:
      now_id = sub_ids.pop(0)
      totalImportanceValue += employees[idToEmployeesIndex[now_id]].importance
      sub_ids.extend(employees[idToEmployeesIndex[now_id]].subordinates)
    return totalImportanceValue
