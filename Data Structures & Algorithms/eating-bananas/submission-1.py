# import math
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
#         n=max(piles)
#         i,j=0,n
#         res=n
#         while i<=j:
#             k=(i+j) // 2
#             cons=0
#             for i in range(0,len(piles)):
#                 cons+=math.ceil(piles[i]/k)
#             if cons > h:
#                 i=k+1
#             else:
#                 res=k
#                 j=k-1
#         return 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res