/**
 * @param {number[]} nums
 * @return {number[][]}
 */

const threeSum = (nums) => {
  nums.sort((a, b) => a - b)
  return nums
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
