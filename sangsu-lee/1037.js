/**
 * @param {number[][]} points
 * @return {boolean}
 */
String.prototype.format = function () {
  var i = 0, args = arguments;
  return this.replace(/{}/g, function () {
    return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};

let areDistinctPoints = function(points) {
    let distinctarr = [];
    points.map(point => {
        distinctarr.push(point[0] + point[1]/1000);
    })
    console.log(distinctarr);
    let set = new Set(distinctarr);
    console.log(set);
    console.log("set.size: {}".format(set.size));
    console.log("arr.size: {}".format(points.length));
    if (set.size == points.length) {
        return true;
    }
    return false;
}

let isInSameLine = function(points) {
    for (let point of points) {
        if (point[0] != point[1]) {
            return false;
        }
    }
    return true;
}


let isBoomerang = function(points) {
    xs = []; ys = []
    points.map(point => {
        xs.push(point[0]); ys.push(point[1]);
    });
    if (!isInSameLine(points) && areDistinctPoints(points)) {
        return true;
    } else {
        return false;
    }
};
console.log(isBoomerang([[0,0],[0,2],[2,1]]));
console.log(isBoomerang([[0,0],[2,1],[2,1]]));
