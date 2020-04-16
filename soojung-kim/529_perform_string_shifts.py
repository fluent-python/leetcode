from typing import List

class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total = 0
        for x in shift:
            direction, amount = x[0], x[1]
            if direction == 1:
                total += amount
            else:
                total -= amount
        total = total % len(s)
        print(total)
        if total > 0:
            return s[-total:] + s[:-total]
        elif total < 0:
            return s[total:] + s[:total]
        elif total == 0:
            return s