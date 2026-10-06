class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}":"{","]":"[",")":"("}
        stack=[]
        for ch in s:
            # print(ch)
            if ch in closeToOpen:
                print(ch)
                if stack and stack[-1]==closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False

        