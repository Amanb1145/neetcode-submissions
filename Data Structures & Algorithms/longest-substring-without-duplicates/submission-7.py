class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ht={}
        ml=0
        left=0
        current_length=0
        for i in range(len(s)):
            if s[i] in ht:
                while(s[i] in ht):
                    ht.pop(s[left])
                    left += 1
            current_length = i - left + 1
            ht[s[i]]=ht.get(s[i],0)+1
            ml=max(ml,current_length)
            
        return max(ml,current_length)
