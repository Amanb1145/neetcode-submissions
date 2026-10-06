class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        pro=1
        for i in range(len(nums)):
            left[i]=pro
            pro=pro*nums[i]
        right=[1]*len(nums)
        pro=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=pro
            pro=pro*nums[i]
        l=[]
        for i in range(len(nums)):
            l.append(left[i]*right[i])
        return(l)