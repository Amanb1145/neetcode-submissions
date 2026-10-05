class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        oldcount=0
        lastn=0
        for i in nums:
            if i == 1:
                count+=1
            else:
                if count > oldcount:
                    oldcount=count
                    count=0
                else:
                    count = 0
        return max(count,oldcount)
                

            
        