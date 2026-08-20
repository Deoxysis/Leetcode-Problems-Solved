class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

        inorder(root)

        def build_tree(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            node = TreeNode(arr[mid])
            node.left = build_tree(l, mid - 1)
            node.right = build_tree(mid + 1, r)
            return node

        return build_tree(0, len(arr) - 1)
