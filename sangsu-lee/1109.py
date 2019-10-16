from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        s = [0] * (n + 1)
        for i, j, k in bookings:
            s[i - 1] += k
            s[j] += -k
        for i in range(1, n):
            s[i] += s[i - 1]
        return s[:-1]
