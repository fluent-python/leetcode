/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsets = (nums) => {
  if (nums.length == 0) return [];
  if (nums.length == 1) return [nums, []];
  const ss = subsets(nums.slice(1));
  const include_first = ss.map(arr => arr.concat(nums[0]));
  return ss.concat(include_first);
};

console.log(subsets([1, 2, 3]));

