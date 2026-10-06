class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            if s==t:
                return True
            else:
                return False
        i=0
        j=0
        count=0
        while(j<len(t)):
            if len(s)==i:
                return True
            if s[i]==t[j]:
                count+=1
                i+=1
            j+=1
        if count==len(s):
            return True
        else:
            return False
        