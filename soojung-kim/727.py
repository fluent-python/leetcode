# how to solve
# 1. 리스트 형태의 입력값의 중복값을 제거하고 리스트의 길이를 반환하는 문제라고 이해
# 2. 조건은 inplace with O(1) extra memory
# 3. enumerate로 리스트를 순회하면서 tmp값에 int저장하고 tmp값이 동일하면 그 리스트의 인덱스 제거

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        idx = 0
        num = nums[idx]
        while idx < len(nums)-1:
            tmp_num = nums[idx+1]
            if num == tmp_num:
                nums.pop(idx+1)
            else:
                num = tmp_num
                idx += 1
        return len(nums)


if __name__ == '__main__':
    result = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(result)
    assert result == 5, "Failed"
