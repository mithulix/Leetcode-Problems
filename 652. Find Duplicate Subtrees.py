class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        tree_map = {}

        def dfs(node, path):
            if not node:
                return "#"
            path += ",".join([str(node.val), dfs(node.left,
                             path), dfs(node.right, path)])
            if path in tree_map:
                tree_map[path] += 1
                if tree_map[path] == 2:
                    res.append(node)
            else:
                tree_map[path] = 1
            return path
        dfs(root, "")
        return res
ts to save