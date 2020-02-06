/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

const findPivot = (nums, s, e) => {
  // array that findPivot() returns true: [1, 2, 3]
  // array that findPivot() returns false: [1] or [4, 1, 2, 3]
  if (e - s <= 1 || nums[e] - nums[e] <= 0) return false;
  if (e - s == 2 && nums[s] > nums[e]) return s;
  if (nums[e] - nums[s] > 0) return true;
  const left_ret = findPivot(nums, s*2, e);
  if (typeof(left_ret) === 'number') return left_ret
  if (typeof(right_ret) === 'number') return right_ret

  if (nums[0])
}
const search = (nums, target) => {
  const pivot = findPivot(nums);
};
