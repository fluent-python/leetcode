
class Solution:
    def hasFloatingPoint(self, x):
        return str(x).split('.')[1] == '0'

    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        n = num
        while n != 1:
            if self.hasFloatingPoint(n / 2.):
                n /= 2.
            elif self.hasFloatingPoint(n / 3.):
                n /= 3.
            elif self.hasFloatingPoint(n / 5.):
                n /= 5.
            else:
                return False

        return True

s = Solution()
