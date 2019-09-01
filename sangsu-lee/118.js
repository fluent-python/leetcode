/**
 * @param {number} numRows
 * @return {number[][]}
 */
let dp_fac = new Array(10000).fill(-1);
let factorial = function(x) {
    if ( x == 0 || x == 1 ) {
        return 1;
    }
    if ( dp_fac[x] != -1 ) {
        return dp_fac[x];
    }
    return x * factorial(x - 1);
};

let nCr = function(n, r) {
    if (n == 0 || r == 0 || n == r) return 1;
    return factorial(n) / factorial(n-r) / factorial(r);
}

let generate = function(numRows) {
    let ret = [];
    for (let i = 0; i < numRows; i++) {
        let row = [];
        for (let j = 0; j <= i; j++) {
            const ncr = nCr(i, j);
            row.push(ncr);
        }
        ret.push(row);
    }
    return ret;
};


