/**
 * @param {string} s
 * @return {string}
 */

const checkPalindrom = (s) => {
  let st = 0;
  let end = s.length - 1;
  while (st + 1 <= end) {
    if (s[st] != s[end]) {
      return false;
    }
    st += 1;
    end -= 1;
  }
  return true;
}
const longestPalindrome = (s) => {
  if (!s) return ''
  for (let wsize = s.length; wsize > 0; wsize--) {
    for (let i = 0; i <= s.length - wsize; i++) {
      const substring = s.slice(i, i + wsize);
      if (checkPalindrom(substring)) return substring
    }
  }
};
