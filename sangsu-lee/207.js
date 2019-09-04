/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
let isItemInStack = function(stack, item) {
    return stack.includes(item)
}
let canFinish = function(numCourses, prerequisites) {
    let visited = new Array(numCourses).fill(0);
    let adj = new Array(numCourses).fill(-1).map(() => new Array(numCourses).fill(-1));
    for (let list of prerequisites) {
        let [from, to] = list
        adj[from][to] = 1;
    }
    console.log(adj);
    let stack = [];
    let start = prerequisites[0][0];
    stack.push(start);
    visited[start] = 1;
    while (stack.length > 0) {
        cur = stack.pop()
        console.log(cur);
        for (let i = 0; i < numCourses; i++) {
            if (adj[cur][i] == 1 && !visited[i]) {
                if (isItemInStack(stack, i)) {
                    return false;
                }
                stack.push(i);
                visited[i] = 1;
            }
        }
    }
    console.log(visited);
    return true
};

ret = canFinish(2, [[1,0],[0,1]] )
console.log("ret: " + ret);
