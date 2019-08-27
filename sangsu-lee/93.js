/**
 * @param {string} s
 * @return {string[]}
 */

let validateSubstrings = function(arrayOfStrings) {
    for (string of arrayOfStrings) {
        if (parseInt(string) > 255 || parseInt(string) < 0) {
            return false;
        }
        if (string.length > 1 && string.startsWith('0')) {
            return false;
        }
    }
    return true;
}

let restoreIpAddresses = function(s) {
    if (s.length < 4 || s.length > 12) return [];
    let dotSpace = s.length - 1;
    let ret = [];
    for (let i = 1; i <= dotSpace - 2; i++) {
        for (let j = i+1; j <= dotSpace - 1; j++) {
            for (let k = j+1; k <= dotSpace; k++) {
                let arrayOfStrings = [s.slice(0, i), s.slice(i, j), s.slice(j, k), s.slice(k, s.length)]
                if (validateSubstrings(arrayOfStrings)) {
                    ret.push(arrayOfStrings.join('.'))
                }
            }
        }
    }
    return ret;
};

console.log(restoreIpAddresses('010010'));
