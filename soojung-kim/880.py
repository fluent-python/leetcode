class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = x * -1
            x = -int(str(x)[::-1])
        else:
            x = int(str(x)[::-1])
        if abs(x) >= pow(2, 31)-1:
            return 0
        return x


if __name__ == '__main__':
    result = Solution().reverse(-16469)
    print(result)

