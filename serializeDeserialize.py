# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        q = deque()
        q.append(root)
        res = []
        while q:
            qSize = len(q)
            for i in range(qSize):
                par = q.popleft()
                if par:
                    res.append(str(par.val))
                    q.append(par.left)
                    q.append(par.right)
                else:
                    res.append("#")
        print(",".join(res))
        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = data.split(",")
        ptr = 0
        q = deque()
        mainRoot = TreeNode(data[0])
        q.append(mainRoot)
        ptr += 1

        while q:
            qSize = len(q)
            for i in range(qSize):
                root = q.popleft()
                lchild = int(data[ptr]) if data[ptr] != "#" else None
                root.left = TreeNode(data[ptr]) if lchild != None else None
                ptr += 1
                rchild = int(data[ptr]) if data[ptr] != "#" else None
                root.right = TreeNode(rchild) if rchild != None else None
                ptr += 1
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
    
        return mainRoot
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))