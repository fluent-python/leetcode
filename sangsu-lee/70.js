/**
 * @param {number} n
 * @return {number}
 */

// Math.trunc()로 casting을 해보려다가 망했다 계속 답이
// 1 차이, 2 차이 등이 생겼음. Math.round로 고치니 됨. ㅎ ㅏ ..

String.prototype.format = function () {
  let i = 0, args = arguments;
  return this.replace(/{}/g, function () {
    return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};

memo = new Array(10000).fill(-1);
memo[0] = 1; memo[1] = 1; memo[2] = 2;

let f = function(n) {
    if (memo[n] != -1) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;
    memo[n] = n * f(n-1);
    return memo[n];
};

let nCr = function(n, r) {
    if (r == 0 || n == r) return 1;
    const ret = f(n) / (f(n-r) * f(r));
    return ret
};

let climbStairs = function(n) {
    let start = Math.trunc(Math.ceil(n/2));
    let _r = 0;
    if (n % 2 == 1) {
        _r = 1;
    }
    let end = n + 1;
    let answer = 0;

    for (let n = start; n < end; n++) {
        answer += nCr(n, _r);
        _r += 2;
    }
    return Math.round(answer);
};

console.log(climbStairs(35));
