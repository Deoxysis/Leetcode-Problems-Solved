class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        NUM_NODES = 26

        distance_matrix = [[INF] * NUM_NODES for _ in range(NUM_NODES)]

        for i in range(NUM_NODES): #set diagonals to zero
            distance_matrix[i][i] = 0
        for index in range(len(original)): #fill transformations
            source_char = original[index]
            destination_char = changed[index]
            transformation_cost = cost[index]

            source_index = ord(source_char) - ord('a')
            destination_index = ord(destination_char) - ord('a')
            #consider minimum if distances repeat
            distance_matrix[source_index][destination_index] = min(     
                distance_matrix[source_index][destination_index],
                transformation_cost
                )
        for intermediate in range(NUM_NODES):
            for start in range(NUM_NODES):
                if distance_matrix[start][intermediate] != INF:
                    for end in range(NUM_NODES):
                        if distance_matrix[intermediate][end] != INF:
                            distance_matrix[start][end] = min(
                                distance_matrix[start][end],
                                    distance_matrix[start][intermediate] + distance_matrix[intermediate][end]
                                )
        cost = 0
        i = 0
        while(i < len(source)):
            src = ord(source[i]) - ord('a')
            dest = ord(target[i]) - ord('a')
            cost += distance_matrix[src][dest]
            i += 1
        if cost == float('inf'): return -1
        return cost




        