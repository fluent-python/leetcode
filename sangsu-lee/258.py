class Solution:
    def addDigits(self, num: int) -> int:
        cur = sum([int(c) for c in str(num)])
        if len(str(cur)) == 1:
            return cur
        else:
            return self.addDigits(cur)

s = Solution()
print(s.addDigits(38))
