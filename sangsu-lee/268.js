/**
 * @param {number[]} nums
 * @return {number}
 */
let missingNumber = function(nums) {
    let max = Math.max.apply(null, nums)
    freq_arr = new Array(max + 2).fill(0);
    for (num of nums) {
        freq_arr[num] = 1;
    }
    for (let i = 0; i < freq_arr.length; i++) {
        if (freq_arr[i] == 0) return i;
    }
};

console.log(missingNumber([4, 1, 2, 3, 0]));
