/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
const postorderTraversal = (root) => {
    if (root === null) return [];
    return postorderTraversal(root.left).concat(postorderTraversal(root.right)).concat(root.val)
};
