
const merge = (intervals) => {
  const ans = [];
  if (intervals.length == 1) return intervals;
  let i = 0;
  for (let j = i + 1; j < intervals.length; j++) {
    const is = intervals[i][0], ie = intervals[i][1];
    const js = intervals[j][0], je = intervals[j][1];
    if (ie >= js) continue;
    ans.push([is, intervals[j-1][1]]);
    i = j;
  }
  return ans
};

console.log(merge([[1,3],[2,6],[8,10],[15,18]]))
