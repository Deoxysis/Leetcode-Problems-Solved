import heapq
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        asteroids.sort()
        
        while(len(asteroids) > 0):
            max_idx = bisect.bisect(asteroids, mass)
            if max_idx == 0:
                return False
            elem = asteroids[max_idx - 1]
            mass += elem
            del asteroids[max_idx - 1]
        
        return True