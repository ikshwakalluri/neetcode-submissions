class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        for i in range(len(tokens)):
         if tokens[i]=="+":
            temp=int(stack[-2])+int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
         elif tokens[i]=="/":
            temp=int(stack[-2])/int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
         elif tokens[i]=="-":
            temp=int(stack[-2])-int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
         elif tokens[i]=="*":
            temp=int(stack[-2])*int(stack[-1])
            stack.pop()
            stack.pop()
            stack.append(temp)
         else:
            stack.append(tokens[i])

        return int(stack[0])
        


        