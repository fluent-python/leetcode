/** Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
 * @param {number[]} nums
 * @return {number[][]}
 */
let permute = function(nums) {
    if (nums.length <= 1) return [nums];

    const ret = [];
    for (let i = 0; i < nums.length; i++) {
        let left_arr = nums.slice(0, i);
        let target = [nums[i]];
        let right_arr = nums.slice(i + 1);

        let rest = left_arr.concat(right_arr);
        arr_of_arr = permute(rest);
        for (const arr of arr_of_arr) {
            ret.push(target.concat(arr))
        }
    }
    return ret;
};

console.log(permute([1, 2, 3]));
