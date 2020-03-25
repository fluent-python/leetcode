from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int(''.join(map(str, digits)))+1))


if __name__ == '__main__':
    result = Solution().plusOne([1,2,3])
    print(result)
