class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = "".join(c.lower() for c in s if c.isalnum())
        a=0
        c=len(f)-1
        b=len(f)//2
        boo = True
        while(a<b):
            if f[a]==f[c]:
                a+=1
                c-=1
            else:
                boo=False
                break
        return boo
        