/**
 * @param {string} s
 * @return {number}
 */ Brute force
const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;
  for (let i = Math.min(s.length, 96); i > 0; i--) {
    for (let j = 0; j <= s.length - i; j++) {
      const set = new Set([]);
      for (let k = j; k < j + i; k++) {
        if (set.has(s[k])) break;
        set.add(s[k])
      }
      if (set.size === i) return i;
    }
  }
};
