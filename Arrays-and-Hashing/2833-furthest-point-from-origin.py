class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        counts = [0,0] #l-r, _
        for direction in moves:
            if direction == 'L':
                counts[0] += 1
            elif direction == 'R':
                counts[0] -= 1
            else:
                counts[1] += 1
        return abs(counts[0]) + counts[1]