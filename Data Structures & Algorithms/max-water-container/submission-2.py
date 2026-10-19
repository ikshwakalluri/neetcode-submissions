class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        volume=0
        while i < j:
            h=min(heights[i],heights[j])
            w=(j-i)
            volume=max(volume,h*w)
            if heights[i]>heights[j]:
                j-=1
            elif heights[i]<heights[j]:
                i+=1
            else:
                i+=1
                j-=1  
        return volume
        