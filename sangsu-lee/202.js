/**
 * @param {number} n
 * @return {boolean}
 */

const isHappy = n => {
  const set = new Set([]);

  let cur = n;
  while ((!set.has(cur)) && cur !== 1) {
    set.add(cur);
    let sum = 0;
    for (let d of cur.toString()) {
      sum += Math.pow(Number(d), 2);
    }
    cur = sum;
  }
  if (cur === 1) return true;
  else return false;
};

console.log(isHappy(19));
console.log(isHappy(2));
