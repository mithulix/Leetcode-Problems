/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
 let leafSimilar = (A, B, leaves = {A: [], B: [] }) => {
    let go = (root, leaves = []) => {
        if(!root)
        return;
        if(!root.left && !root.right)
        leaves.push(root.val);
        go(root.left, leaves);
        go(root.right, leaves);
    };
    go(A, leaves.A);
    go(B, leaves.B);
    go(C, leaves, C);
    return leaves.A.join(',') == leaves.B.join(',');
};