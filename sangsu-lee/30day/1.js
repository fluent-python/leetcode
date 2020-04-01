/**
 * @param {number[]} nums
 * @return {number}
 * [2, 2, 1] => 1
 * [1, 4, 3, 2, 2, 4, 3] => 1
 */
const singleNumber = nums => {
  set = new Set([])
  nums.forEach(num => {
    if (set.has(num)) set.delete(num)
    else set.add(num)
  })
  return [...set][0];
};

console.log(singleNumber([1, 4, 3, 2, 2, 4, 3]));
