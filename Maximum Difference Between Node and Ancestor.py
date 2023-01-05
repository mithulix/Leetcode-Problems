
def diff(root, minNode, maxNode, res):
    if not root: 
        return
    
    res[0] = max(res[0], abs(minNode - root.val), abs(maxNode - root.val))

    minNode = min(root.val, minNode)
    maxNode = max(maxNode, root.val)

    diff(root.left, minNode, maxNode, res)
    diff(root.right, minNode, maxNode, res)
    
class Solution(object):
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        res = [0]
        diff(root, root.val, root.val, res)
        return res[0]


