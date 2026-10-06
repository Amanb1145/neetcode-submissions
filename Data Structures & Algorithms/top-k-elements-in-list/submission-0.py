class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq={}
        for i in nums:
            if i in frq:
                frq[i]=frq.get(i,0)+1
            else:
                frq[i]=1
        l=[]
        nfrq=sorted(frq.items(), key=lambda x: x[1], reverse=True)
        for key,value in nfrq:
            if len(l)<k:
                l.append(key)
        return(l)