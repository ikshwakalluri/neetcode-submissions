class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in range(len(s)):
            if 65<=ord(s[i])<=92 or 97<=ord(s[i])<=122 or 48<=ord(s[i])<= 57:
                res+=s[i].lower()
        return res==res[::-1]