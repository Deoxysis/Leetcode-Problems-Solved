from collections import deque

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [set() for _ in range(n)]

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        ans = 0

        for node in range(n):
            if node in visited:
                continue

            queue = deque([node])
            visited.add(node)

            num_nodes = 0
            num_edges = 0

            while queue:
                u = queue.popleft()
                num_nodes += 1

                num_edges += len(graph[u])

                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)

            # Each edge was counted twice
            num_edges //= 2

            if num_edges == num_nodes * (num_nodes - 1) // 2:
                ans += 1

        return ans