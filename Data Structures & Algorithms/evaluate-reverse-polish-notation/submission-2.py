class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
                "+": lambda a, b: a + b,
                "-": lambda a, b: a - b,
                "*": lambda a, b: a * b,
                "/": lambda a, b: a / b
            }
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in ops:
                temp=ops[tokens[i]](stack[-2],stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(temp))
            else:
                stack.append(int(tokens[i]))
        return int(stack[-1])