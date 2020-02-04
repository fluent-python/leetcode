/**
 * @param {string} s
 * @return {string}
 */

dp = Array(1001).fill(0).map(x => Array(1001).fill(0))
let maxlenLo = 0, maxLen = 0;
const longestPalindrome = (s) => {
  for (let hi = 0; hi < s.length; hi++) {
    for (let lo = 0; lo <= hi; lo++) {
      dp[lo][hi] = ((s[lo] === s[hi]) && (hi - lo < 3 || dp[lo+1][hi-1])) ? 1 : 0;
      if (dp[lo][hi] && (hi-lo+1 > maxLen)) {
        maxlenLo = lo; 
        maxLen = hi - lo + 1;
      }
    }
  }
  return s.slice(maxlenLo, maxlenLo + maxLen);
};
