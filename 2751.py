class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        indices = list(range(n))
        indices.sort(key=lambda i: positions[i])

        stack = []

        #we'll set the destroyed robots' health to zero 
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack.pop()#pop the right moving robot

                    #simply follow conditions
                    if healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                        stack.append(j)

                    elif healths[j] < healths[i]:
                        healths[i] -= 1
                        healths[j] = 0

                    else:
                        healths[i] = 0
                        healths[j] = 0

        return [h for h in healths if h > 0]