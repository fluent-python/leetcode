/**
 * Definition for a binary tree node.
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

String.prototype.format = function() {
  let i = 0, args = arguments;
  return this.replace(/{}/g, function() {
    return typeof args[i] != 'undefined' ? args[i++] : '';
  });
};

let inorderTraversal = function(root) {
    if (root == null) {
        return [];
    }
    return inorderTraversal(root.left)
            .concat([root.val])
            .concat(inorderTraversal(root.right));
};

let node = new TreeNode(1);
node.right = new TreeNode(2);
node.right.left = new TreeNode(3);

console.log(inorderTraversal(node));

