/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */

const findOrder = (numCourses, prerequisites) => {
  const v = new Array(numCourses).fill(null).map(x => []);
  const visited = new Array(numCourses).fill(false);
  const isRoot = new Array(numCourses).fill(true);

  for (let [to, from] of prerequisites) {
    v[from].push(to);
    isRoot[to] = false;
  }
  console.log(v);
  console.log(isRoot);
  isRoot.forEach((x, i) => {
    if (!x) return;

    // Do bfs
    q = [i];
    while (q.length > 0) {
      const cur = q.shift();
      console.log(`cur: ${cur}`);
      v[cur].forEach(to => {
        if (!visited[to]) {
          q.push(to);
          visited[to] = true;
          console.log(`push ${to}`);
        }
      })
    }
    console.log(i);
  })


};

findOrder(4, [[1,0],[2,0],[3,1],[3,2]]);
