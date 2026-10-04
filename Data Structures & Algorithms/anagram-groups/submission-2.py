class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ascii_list=defaultdict(list) # ASCI to list of strs
        for s in strs:
            alpha=[0]*26
            for c in s:
                alpha[ord(c)-ord("a")]+=1
            ascii_list[str(alpha)].append(s)
        
        return list(ascii_list.values())




