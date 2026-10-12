class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in ('(', '[', '{'):
                st.append(i)
            else:
                if len(st)!=0:
                    pass
                else:
                    return False
                eb=pairs[i]
                if st[-1]==eb:
                    st.pop(-1)
                else:
                    return False
        if len(st)==0:
            return True
        else:
            return False