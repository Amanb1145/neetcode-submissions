class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         s = nums[i]+nums[j]
        #         if s == target:
        #             return [i,j]
        # return "Not Found"
        hm_prv = {}
        for i, num in enumerate(nums):
            if target-num in hm_prv:
                return [hm_prv[target-num], i] 
            hm_prv[num]=i

        
        