from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # dfs
        dic = defaultdict(set)
        neigh = defaultdict(set)

        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)

        stack = [i for i in range(numCourses) if not dic[i]]
        res = []
        while stack:
            pre = stack.pop()
            res.append(pre)
            for i in neigh[pre]:
                dic[i].remove(pre)
                if not dic[i]:
                    stack.append(i)
            dic.pop(pre)
        return res if not dic else []