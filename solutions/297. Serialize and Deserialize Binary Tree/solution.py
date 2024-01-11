class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.preorder_str = []
        def preorder(root):
            if not root:
                self.preorder_str.append('N')    
                return
            self.preorder_str.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ','.join(self.preorder_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        self.index = 0

        def dfs():
            if preorder[self.index] == 'N':
                self.index += 1
                return
            node = TreeNode(preorder[self.index])
            self.index += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
