# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append(root)
        q.append(0) #column number
        minCol, maxCol = 0, 0 
        columnMap = defaultdict(list)


        res = []
        while q:
            root = q.popleft()
            col = q.popleft()
            columnMap[col].append(root.val)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)

            if root.left:
                q.append(root.left)
                q.append(col - 1)
            if root.right:
                q.append(root.right)
                q.append(col + 1)
        
        for i in range(minCol, maxCol + 1):
            res.append(columnMap[i])
        return res
            
            

