/**
 * @param {number[]} bits
 * @return {boolean}
 */
let isOneBitCharacter = function(bits) {
    let ptr = bits.length == 1 ? 0 : bits.indexOf(1);
    while (ptr <= bits.length - 1) {
        if (bits[ptr] == 0) {
            if (ptr == bits.length - 1) return true;
            ptr++;
        } else {
            ptr += 2;
        }
    }
    return false;
};

console.log(isOneBitCharacter([1, 0, 0]));
console.log(isOneBitCharacter([1, 1, 1, 0]));

