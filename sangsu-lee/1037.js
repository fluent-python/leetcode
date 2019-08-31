/**
 * @param {number[][]} points
 * @return {boolean}
 */
let isBoomerang = function(points) {
    let ps = points
    let [x1, x2, x3, y1, y2, y3] = [ps[0][0], ps[1][0], ps[2][0],
                                    ps[0][1], ps[1][1], ps[2][1]]
    if ((x1 == x2 && y1 == y2)
     || (x2 == x3 && y2 == y3)
     || (x3 == x1 && y3 == y1)) return false;
    let slope1 = (x1 - x2) / (y1 - y2)
    let slope2 = (x2 - x3) / (y2 - y3)
    let slope3 = (x3 - x1) / (y3 - y1)
    
    if (slope1 == slope2 || slope2 == slope3 || slope1 == slope3) return false;
    return true;

    console.log(slope1, slope2, slope3);
};

console.log(isBoomerang([[0,1],[0,1],[2,1]]));
