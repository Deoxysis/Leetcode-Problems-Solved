# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        traversal = list()

        def inorder(node : List[int], trav : List[int]):
            if node is not None:
                inorder(node.left, trav)
                trav.append(node.val)
                inorder(node.right, trav)
        
        inorder(root, traversal)
        return traversal
