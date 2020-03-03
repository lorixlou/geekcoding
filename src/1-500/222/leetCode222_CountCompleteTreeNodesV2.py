# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0 
        # if left tree hight = right tree hight = h,  then it has 2^h - 1 nodes 
        # if not, then recursive 
        lheights = {}
        rheights = {}

        hL = self.hightLeft( root.left, lheights)
        hR = self.hightRight( root.right, rheights)
        if hL == hR :
            return 2**(hL + 1) - 1 
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 

    def hightLeft(self, root: TreeNode, heights : dict) -> int:
        
        if not root:
            return 0

        if root.left   in heights:
            h = heights[root.left]
        else:    
            h = self.hightLeft( root.left, heights) 
            heights[root.left] = h 
        
        return h + 1 
     
    def hightRight(self, root: TreeNode,heights) -> int:
        if not root:
            return 0

        if root.right   in heights:
            h = heights[root.right]
        else:    
            h = self.hightRight( root.right, heights) 
            heights[root.right] = h 
        
        return h + 1
