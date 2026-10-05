from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter=Counter(nums) #O(n)
        bucket=[[] for _ in range(len(nums)+1)]
        res=[]
        for key,value in freq_counter.items():
            bucket[value].append(key)
        
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res


            
        