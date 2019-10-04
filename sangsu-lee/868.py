class Solution:
    def binaryGap(self, N: int) -> int:
        binary = "{0:b}".format(N)
        distance = 0
        while '1' in binary[1:]:
            one_ix = binary[1:].index('1') + 1
            if (distance < one_ix):
                distance = one_ix
            binary = binary[one_ix:]
        return distance


s = Solution()
s.binaryGap(6)
