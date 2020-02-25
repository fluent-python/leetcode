/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
const zigzagLevelOrder = (root) => {
  const maxDepth = Math.log(Math.sqrt(root.length)) / Math.log(2);
  console.log('maxDepth: ', maxDepth);
};

zigzagLevelOrder(new Array(8));
