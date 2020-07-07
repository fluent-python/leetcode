class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

if __name__ == '__main__':
    res = Solution().hammingDistance(1, 4)
    print(res)