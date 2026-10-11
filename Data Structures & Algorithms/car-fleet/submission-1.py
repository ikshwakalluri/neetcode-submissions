class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posMapspeed=sorted(zip(position,speed),reverse=True)
        stack=[]
        for pos,speed in posMapspeed:
            t=(target-pos)/speed
            if not stack or t>stack[-1]:
                stack.append(t)
        return len(stack)

        
        