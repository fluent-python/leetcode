/**
 * @param {number[][]} wall
 * @return {number}
 */
String.prototype.format = function () {
  var i = 0, args = arguments;
  return this.replace(/{}/g, function () {
    return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};

let leastBricks = function(wall) {
    const wall_length = wall[0].reduce((a, b) => a + b)
    const wall_height = wall.length;
    let brick_sums = new Array(wall_height).fill(0);
    let brick_pos = new Array(wall_height).fill(1);
    for (let i = 0; i < wall_height; i++) {
        brick_sums[i] = wall[i][0];
    }
    let ans = wall_height;

    for (let cur = 1; cur < wall_length; cur++) {
        let n_cut = 0;
        for (let i = 0; i < wall_height; i++) {
            if (cur == brick_sums[i]) {
                brick_sums[i] += wall[i][brick_pos[i]++];
            }
            else {
                n_cut++;
            }
        }
        if (n_cut < ans) {
            ans = n_cut;
        }
    }
    return ans
};
ret = leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]);
