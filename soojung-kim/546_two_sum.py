from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums = sorted(nums)
        if sort_nums[0] < 0: filter_nums = nums
        else: filter_nums = list(filter(lambda x: x<=target, nums))

        diff_idx = 0
        pivot = 0
        i = 0
        while i < len(filter_nums)-1:
            pivot = filter_nums[i]
            diff = target - pivot
            if diff in filter_nums[i+1:]:
                diff_idx = diff
                if pivot == diff:
                    return [i for i, item in enumerate(nums) if item == pivot]
                break
            else:
                i += 1
        return list((nums.index(pivot), nums.index(diff_idx)))


if __name__ == '__main__':
    nums = [230,863,916,585,981,404,316,785,88,12,70,435,384,778,887,755,740,337,86,92,325,422,815,650,920,125,277,336,221,847,168,23,677,61,400,136,874,363,394,199,863,997,794,587,124,321,212,957,764,173,314,422,927,783,930,282,306,506,44,926,691,568,68,730,933,737,531,180,414,751,28,546,60,371,493,370,527,387,43,541,13,457,328,227,652,365,430,803,59,858,538,427,583,368,375,173,809,896,370,789]
    target = 542
    result = Solution().twoSum(nums, target)
