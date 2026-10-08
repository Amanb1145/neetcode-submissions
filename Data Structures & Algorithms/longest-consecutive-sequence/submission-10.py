class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        series=sorted(set(nums))
        count=1
        prv=series[0]
        countl=[]
        for i in series:
            if i == prv:
                pass
            else:
                if i==prv+1:
                    prv=i
                    count+=1
                else:
                    countl.append(count)
                    count=1
                    prv=i
        if len(countl)==0:
            return count
        if count > max(countl):
            return count
        else:
            return max(countl)
        
        