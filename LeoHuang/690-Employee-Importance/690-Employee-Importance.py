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
    while len(sub_ids) != 0:
      now_id = sub_ids.pop(0)
      i = 0
      while now_id != employees[i].id:
        i += 1
      totalImportanceValue += employees[i].importance
      sub_ids.extend(employees[i].subordinates)
    return totalImportanceValue
