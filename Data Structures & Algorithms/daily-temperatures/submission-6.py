class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for index,value in enumerate(temperatures):
            while stack and value > temperatures[stack[-1]]:
                prev_ind=stack.pop()
                res[prev_ind]=index-prev_ind
            stack.append(index)
        return res
        
            

        