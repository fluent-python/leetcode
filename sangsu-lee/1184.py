from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        if start > destination:
            start, destination = destination, start
        print("clockwise: {}".format(sum(distance[start:destination])))
        print("cclockwise: {}".format(sum(distance[:start] + distance[destination:])))
        return min(sum(distance[start:destination]),
                   sum(distance[:start]+distance[destination:]))

s = Solution()
print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 1))
print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 2))
print(s.distanceBetweenBusStops([1, 2, 3, 4], 0, 3))
