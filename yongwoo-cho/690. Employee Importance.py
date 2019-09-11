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
    def _getImp(self, id):
        result = self.importance_dict[id]
        for sub in self.sub_dict[id]:
            result += self._getImp(sub)
        return result
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        result = 0 
        self.importance_dict = {}
        self.sub_dict = {}
        
        for emp in employees:
            self.importance_dict[emp.id] = emp.importance
            self.sub_dict[emp.id] = emp.subordinates
        
        result = self._getImp(id)
        return result
                
        
