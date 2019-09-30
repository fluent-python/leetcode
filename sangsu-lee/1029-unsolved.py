from typing import List
from itertools import combinations


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        As, Bs = list(map(list, zip(*costs)))
        As = sorted(As)
        Bs = sorted(Bs)
        print(As, Bs)
        print( sum(As[:len(costs)//2]))
        print(sum(Bs[:len(costs)//2]))

s = Solution()
s.twoCitySchedCost([[289,393],[484,287],[317,704],[192,126],[699,429],[100,85],[482,352],[976,727],[240,569],[621,492],[189,936],[437,616],[597,458],[703,858],[258,923],[524,558],[240,502],[861,228],[840,463],[130,742],[653,402],[836,430]])
s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])

