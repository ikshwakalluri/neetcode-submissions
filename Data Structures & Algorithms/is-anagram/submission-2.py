from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        s=sorted(list(s))
        t=sorted(list(t))
        if s!=t:
            return False
        return True
        