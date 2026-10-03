class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for i in range(len(strs)):  
            enc+=f"{len(strs[i])}"+"#"+strs[i]
        return enc
    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        while i < len(s):
            j=s.find('#',i)
            length=int(s[i:j])

            start=j+1
            end=start+length
            dec.append(s[start:end])
            i=end
        return dec
