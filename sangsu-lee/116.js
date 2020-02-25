/**
 * // Definition for a Node.
 * function Node(val, left, right, next) {
 *    this.val = val === undefined ? null : val;
 *    this.left = left === undefined ? null : left;
 *    this.right = right === undefined ? null : right;
 *    this.next = next === undefined ? null : next;
 * };
 */
/**
 * @param {Node} root
 * @return {Node}
 */
const connect = (root) => {
    if (root === null) return null;
    const q = [root];
    let cq = [];
    while (q.length > 0) {
        while (q.length > 0) {
            cq.push(q.shift());
        }
        for (let i = 0; i < cq.length; i++) {
            if (i < cq.length - 1) cq[i].next = cq[i+1];
            if (cq[i].left !== null) q.push(cq[i].left);
            if (cq[i].right !== null) q.push(cq[i].right);
        }
        cq = [];
    }
    return root;
};
