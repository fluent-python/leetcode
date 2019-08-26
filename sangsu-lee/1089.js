/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
let duplicateZeros = function(arr) {
    let zeros_ixs = []
    const orig_length = arr.length;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == 0) zeros_ixs.push(i);
    }
    for (let ix of zeros_ixs.reverse()) {
        arr.splice(ix, 0, 0)
    }
    arr.splice(orig_length);
    console.log(arr)
};

