class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars= sorted(zip(position, speed),reverse=True)

        stack=[]

        for pos,speed in cars:
            time=(target-pos)/speed

            if not stack:
                stack.append(time)
            else:
                if time> stack[-1]:
                    stack.append(time)
                else:
                    continue
        return len(stack)
                