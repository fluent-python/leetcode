from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            largest_stone = max(stones)
            stones.remove(largest_stone)

            second_largest_stone = max(stones)
            stones.remove(second_largest_stone)
            new_weight = largest_stone-second_largest_stone
            if new_weight>=0:
                stones.append(new_weight)
        return stones[0]


if __name__ == '__main__':
    result = Solution().lastStoneWeight([2,2])
    print(result)