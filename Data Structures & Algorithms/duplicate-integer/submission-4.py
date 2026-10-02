class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # ele = {}
        # for i in nums:
        #     ele[i] =  ele.get(i,0) + 1
        #     if ele[i] > 1:
        #         return True
        ele = set()
        for i in nums:
            if i in ele:
                return True
            ele.add(i)
        return False
            
        