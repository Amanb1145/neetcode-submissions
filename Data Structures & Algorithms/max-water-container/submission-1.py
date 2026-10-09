class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxarea=0
        while(i<j):
            lent = j-i
            bre = min(heights[i],heights[j])
            area = lent*bre
            if area>maxarea:
                maxarea=area
            if heights[i]<heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return maxarea