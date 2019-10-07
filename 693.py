class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bins = "{0:b}".format(n)
        if '11' in bins or '00' in bins:
            return False
        return True

s = Solution()

print(s.hasAlternatingBits(16))
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
