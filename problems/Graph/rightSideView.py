# BFS applicartion
# Binary Tree Right Side View
# Leetcode 199: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        output = []
        
        q = collections.deque()
        q.append(root)
        while q:
            r = None
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    r = node
                    q.append(node.left)
                    q.append(node.right)
            if r:
                output.append(r.val)
        return output
        
        