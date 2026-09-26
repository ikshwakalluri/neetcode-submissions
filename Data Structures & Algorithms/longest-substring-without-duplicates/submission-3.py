class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=set()
        l,r=0,0
        output=0
        while r < len(s):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1            
            temp.add(s[r])
            output=max(output,r-l+1)
            r+=1

        return output
        