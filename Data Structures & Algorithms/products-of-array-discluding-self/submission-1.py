class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        # Prefix Product
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        # Suffix
        suffix=[1]*len(nums)
        for i in range(-2,-len(nums)-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(len(nums)):
            nums[i]=prefix[i]*suffix[i]
        return nums