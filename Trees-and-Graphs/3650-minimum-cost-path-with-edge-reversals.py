class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for src, dst, w in edges:
            graph[src].append((dst, w))
            graph[dst].append((src, 2*w))
        import heapq

        def dijkstra_shortest_paths(adjacency_list, start_node):
            shortest_distance = {node: float('inf') for node in adjacency_list}
            shortest_distance[start_node] = 0
            min_priority_queue = [(0, start_node)]
            while min_priority_queue:
                current_distance, current_node = heapq.heappop(min_priority_queue)

                if current_distance > shortest_distance[current_node]:
                    continue

                for neighbor_node, edge_weight in adjacency_list[current_node]:
                    new_distance = current_distance + edge_weight

                    if new_distance < shortest_distance[neighbor_node]:
                        shortest_distance[neighbor_node] = new_distance
                        heapq.heappush(
                            min_priority_queue,
                            (new_distance, neighbor_node)
                        )
            return shortest_distance
        
        try:
            dist = dijkstra_shortest_paths(graph, 0)[n - 1]
            if dist != float('inf'):
                return dist
                
        except:
            return -1
        else:
            return -1
