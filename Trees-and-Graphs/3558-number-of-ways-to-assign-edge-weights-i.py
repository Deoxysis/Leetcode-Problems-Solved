from collections import defaultdict
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        # Create adj list
        tree = defaultdict(list)
        for src, dest in edges:
            tree[src].append(dest)
        
        # find root
        destinations = {dest for src, dest in edges}
        sources = {src for src, dest in edges}
        root = list(sources - destinations)[0]

        def dfs(node) -> int: #find depth max
            if not tree[node]:
                return 0
                
            max_child_depth = 0
            for child in tree[node]:
                max_child_depth = max(max_child_depth, dfs(child))
                
            return max_child_depth + 1

        # Start the operation from the root
        depth = dfs(root)
        return (2**(depth - 1) % (10**9 + 7))

