class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # a = {}
        # for i in s:
        #     a[i] = a.get(i,0)+1
        # print(a)
        # for i in t:
        #     a[i] = a.get(i,0) - 1
        # print(a)
        # for i in a:
        #     if a[i] != 0:
        #         return False
        # return True
        if len(s)!= len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False

        