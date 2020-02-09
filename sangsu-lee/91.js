/**
 * @param {string} s
 * @return {number}
 */
const numDecodings = (s) => {
  if (s.length == 0 || s == null) return 0;
  const dp = new Array(10000).fill(0);
  dp[0] = 1; dp[1] = s[0] != 0 ? 1 : 0
  for (let i = 2; i <= s.length; i++) {
    let a = s.slice(i-1, i);
    let b = s.slice(i-2, i);
    if (a >= 1 && a <= 9) dp[i] += dp[i-1]
    if (b >= 10 && b <= 26) dp[i] += dp[i-2]
  }
  return dp[s.length];
}

// "12321" 이해가 잘 안되네 ...
