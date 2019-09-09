/**
 * @param {number} N
 * @param {number[][]} trust
 * @return {number}
 */
let findJudge = function(N, trust) {
    let inds = new Array(N).fill(0);
    let outds = new Array(N).fill(0);
    for (t of trust) {
        outds[t[0]-1]++;
        inds[t[1]-1]++;
    }

    for (let i = 0; i < N; i++) {
        if (inds[i] == (N-1) && outds[i] == 0) {
            return i+1;
        }
    }
    return -1;
};
ret = findJudge(3, [[1,3],[2,3],[3,1]])
console.log(ret);
ret = findJudge(3, [[1, 2], [2, 3]])
console.log(ret);
ret = findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]])
console.log(ret);
