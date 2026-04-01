class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        
        stack = []  # stores indices of robots moving right
        healths = list(healths)

        for pos, h, d, i in robots:
            if d == 'R':
                stack.append(i)
            else:
                while stack and healths[i] > 0:
                    j = stack[-1]

                    if healths[j] < healths[i]:
                        stack.pop()
                        healths[i] -= 1
                        healths[j] = 0
                    elif healths[j] > healths[i]:
                        healths[j] -= 1
                        healths[i] = 0
                    else:
                        stack.pop()
                        healths[j] = 0
                        healths[i] = 0

        result = []
        for i in range(len(healths)):
            if healths[i] > 0:
                result.append(healths[i])

        return result