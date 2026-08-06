class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for e in invocations:
            graph[e[0]].append(e[1])
        
        #perform dfs
        start = k

        def DFS(Graph, node, visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    DFS(Graph, neighbor, visited)
        
        visited = set()

        DFS(graph, start, visited)
        safe = set()
        for i in range(0, n):
            if i not in visited:
                safe.add(i)

        for src, dest in invocations:
            if src in safe and dest in visited:
                return [i for i in range(n)]
        
        ans = list()
        for i in range(n):
            if i not in visited:
                ans.append(i)
        return ans
